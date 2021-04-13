from django.shortcuts import render
from .models import SumMoney, getPriceFood, GetCount, GetBillId, PrintBill, GetBillInfo, GetDem, GetFoodId, BillId, BillModel, DetailBillModel, DatabaseListBill, PrintBill, SumMoneyBill, GetFoodOrdered
from .serializers import SumMoneySerializer, GetPriceSerializer, GetFoodIdSerializer, GetBillIdSerializer, GetCountSerializer, GetBillInfoSerializer, PrintBillSerializer, BillaSerializer, GetFoodIdSerializer ,GetDemSerializer, BillIdSerializer ,BillSerializer, DetailBillSerializer, ListBillSerializer, PrintBillSerializer, SumMoneyBillSerializer, GetFoodOrderedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from food_table_manager.models import TableModel, FoodModel
from authentication.models import User


# In hóa đơn
class PrintBillView(APIView):

    def get(self, request, pk):
        table_id = pk
        a = 0 
        try:
            a = TableModel.objects.get(id =table_id, status='Có người')
        except:
            a = 0
        if a:
            #print("xin chào")
            bill = PrintBill.objects.raw(f"""SELECT B.id AS "bill_id"
                , B.time_created AS "time_created" , F.food_name AS "food_name"
                , BD.amount AS "amount", BD.price AS "price"
                FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F, food_table_manager_tablemodel TB
                WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id AND TB.id = B.table_id_id AND B.status = false AND TB.id = {table_id}""")
        
            serializer = PrintBillSerializer(bill, many=True)
            billInfo = GetBillInfo.objects.raw(f"""SELECT B.id AS "bill_id", TB.name AS "table_name"
                , to_char(B.time_created, 'YYYY-MM-DD HH:MI:SS') as "time_created"
                , SUM(BD.amount*BD.price) AS "total_price"
                FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F, food_table_manager_tablemodel TB
                WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id AND TB.id = B.table_id_id AND B.status = false AND TB.id = {table_id}
                GROUP BY B.id, TB.name, B.time_created, time_created""")
            bill_Info = GetBillInfoSerializer(billInfo, many=True)
            response = {
                "bill_id": (bill_Info.data[0])['bill_id'],
                "table_name": (bill_Info.data[0])['table_name'],
                "time_created": (bill_Info.data[0])['time_created'],
                "total_price": (bill_Info.data[0])['total_price'],
                "data": serializer.data,
                "status_code": status.HTTP_200_OK
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Not found bill", "status_code": 404}, status=status.HTTP_200_OK)
            
# Thanh toán
class BillPayView(APIView):

    def post(self, request, pk):
        table_id = pk
        table = ''
        try:
            table = TableModel.objects.get(id=table_id, status='Có người')
        except:
            table = ''
        if table=='':
            return Response({"message": "Hóa đơn k có!", "status_code": 404}, status=200)
        if table:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE order_billmodel SET status= true WHERE table_id_id = {table_id}")
                cursor.execute(f"UPDATE food_table_manager_tablemodel SET status='Trống' WHERE id={table_id}")
                return Response({"message": "Payed", "status_code": 200}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Not found bill", "status_code": 404}, status=status.HTTP_200_OK)
            

#Chuyển bàn
class SwitchTableView(APIView):

    def post(self, request):
        table_id_one = request.data['table_one']
        table_id_two = request.data['table_two']

        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE order_billmodel SET table_id_id = {table_id_two} WHERE table_id_id = {table_id_one} AND status=false")
            cursor.execute(f"UPDATE food_table_manager_tablemodel SET status = 'Trống' WHERE id = {table_id_one}")
            cursor.execute(f"UPDATE food_table_manager_tablemodel SET status = 'Có người' WHERE id = {table_id_two}")
        response = {
            "message": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

# Số món ăn bàn đó gọi
class GetOrderedView(APIView):

    def get(self, request, pk):
        order_food_name = GetFoodOrdered.objects.raw(f"""SELECT F.id, F.food_name AS food_name, f.food_price AS food_price, D.amount AS amount
        FROM order_detailbillmodel AS D, food_table_manager_foodmodel AS F, order_billmodel as B 	
        WHERE D.food_id_id = F.id AND D.bill_id_id=B.id and B.status=False and B.table_id_id={pk}""")
        serializer = GetFoodOrderedSerializer(order_food_name, many=True)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

# Gọi món ăn
class OrderFoodView(APIView):

    def getBillID(self, table_id):
        bill_bill = GetBillId.objects.raw(f"""SELECT id AS bill_id FROM order_billmodel 
            WHERE table_id_id = {table_id} 
            AND status=false""")
        billSerializer = GetBillIdSerializer(bill_bill, many=True)
        try:
            return (billSerializer.data[0])['bill_id']
        except:
            return 0

    def getFoodId(self, food_name):
        food_food = GetFoodId.objects.raw(f"""SELECT id AS food_id 
                    FROM food_table_manager_foodmodel 
                    WHERE food_name = '{food_name}'""")
        food_serializer = GetFoodIdSerializer(food_food, many=True)
        try:
            return (food_serializer.data[0])['food_id']
        except:
            return 0

    def getCount(self, food_name, bill_id):
        count_count = GetCount.objects.raw(f"""SELECT COUNT(*)
 AS count FROM order_detailbillmodel AS D, 
                order_billmodel AS B, food_table_manager_foodmodel AS F
                    WHERE D.bill_id_id = B.id AND F.id = D.food_id_id AND B.id = {bill_id} AND F.food_name = '{food_name}'""")
        countSerialzer = GetCountSerializer(count_count, many=True)
        try:
            return (countSerialzer.data[0])['count']
        except:
            return 0

    def post(self, request):
        table_id = request.data['table_id']
        user_id = request.user.id
        foods = request.data['list_food']

        if not foods:
            return Response({"message": "Bạn chưa chọn bàn", "status_code": 400}, status=200)
            
        bill_id = self.getBillID(table_id)
  
        if not bill_id:
            getTable = TableModel.objects.get(id=table_id)
            getUser = User.objects.get(id=user_id)

            bill = BillModel(table_id=getTable, user_id=getUser)
            bill.save()
            
            bill_id = self.getBillID(table_id)
            with connection.cursor() as cursor:
                cursor.execute(f"""UPDATE food_table_manager_tablemodel SET status = 'Có người' WHERE id = {table_id}""")

            #print('XONG DƠT 1')
        if bill_id:
            foods = request.data['list_food']
            for food in foods:
                food_name = food['food_name']
                food_amount = food['amount']
                
                food_id = self.getFoodId(food_name)
                check_food_name = self.getCount(food_name, bill_id)

                if check_food_name:
                    with connection.cursor() as cursor:
                        cursor.execute(f"""UPDATE order_detailbillmodel 
                            SET amount = {food_amount} 
                            WHERE food_id_id={food_id} AND bill_id_id={bill_id}""") 
                    #print('MON AN DA CO') 
                else:
                    # Lấy được food  và bill
                    bill_model = BillModel.objects.get(id = bill_id)
                    food = ''
                    try:
                        food = FoodModel.objects.get(food_name=food_name)
                    except:
                        food = ''
                    if food=='':
                        return Response({"message": "This food not exists!", "status_code": 404}, status=200)
                    food_model = getPriceFood.objects.raw(f"""SELECT food_price FROM food_table_manager_foodmodel WHERE food_name='{food_name}'""")
                    foodSerialzier = GetPriceSerializer(food_model, many=True)
                    food_price = (foodSerialzier.data[0])['food_price']
                    #total_price = int(food_price) * int(food_amount)
                    detail_bill_model = DetailBillModel(bill_id = bill_model, food_id = food, amount = food_amount, price = food_price )
                    detail_bill_model.save()

                    #return Response({"data": (foodSerialzier.data[0])['food_price']}, status=200)
                    # with connection.cursor() as cursor:
                    #     cursor.execute(f"""INSERT INTO order_detailbillmodel(amount, price, bill_id_id, food_id_id) 
                    #         VALUES({food_amount}, (SELECT food_price FROM food_table_manager_foodmodel WHERE id =  {food_id}), {bill_id},  {food_id})""")
                    #print('THEM MOI MON AN')
        response = {         
            "message": "success",
            "status_code": 200
        }
        return Response(response, status=200)