from django.shortcuts import render
from .models import GetDem, GetFoodId, BillId, BillModel, DetailBillModel, DatabaseListBill, PrintBill, SumMoneyBill, GetFoodOrdered
from .serializers import BillaSerializer, GetFoodIdSerializer ,GetDemSerializer, BillIdSerializer ,BillSerializer, DetailBillSerializer, ListBillSerializer, PrintBillSerializer, SumMoneyBillSerializer, GetFoodOrderedSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
# Create your views here.
# class CreateBillView(APIView):
#     def post(self, request):
#         serializer=BillSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response={
#            'data': serializer.data,
#            'status_code': status.HTTP_201_CREATED
#         }
#         return Response(response, status=status.HTTP_201_CREATED)
# class UpdateBillView(APIView):
#     def get_object(self, pk):
#         try: 
#             bill=BillModel.objects.get(pk=pk)
#             return bill
#         except BillModel.DoesNotExist:
#             return Response({"errors":"errors"}, status=404)
#     def get(self, request, pk):
#         bill=self.get_object(pk)
#         serializer=BillSerializer(bill)
        
#         response={
#             "data": serializer.data,
#             "status_code": 200
#         }
#         return Response(response, status=200)

#     # sửa status
#     def put(self, request, pk):

#         status1=request.data['status']
#         with connection.cursor() as cursor:
#             cursor.execute("update order_billmodel set status="+status1+" where id="+str(pk))
#         bill=self.get_object(pk)
#         serializer = BillSerializer(bill)
#         response={
#             "data": serializer.data,
#             "status_code": status.HTTP_200_OK,
#         }
#         return Response(response, status=status.HTTP_200_OK)

class BillPayView(APIView):
    
    def put(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(f"update order_billmodel set status= true where id = {pk}")
        with connection.cursor() as cursor:
            cursor.execute(f"update food_table_manager_tablemodel set status='Trống' where id=(select table_id_id from order_billmodel where id={pk})")
        
        response = {
            "message": "Payed",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)


# class InsertBillInfoView(APIView):
#     def get(self, request):
#         bill_id = request.data['bill_id']
#         detail=DetailBillModel.objects.filter(bill_id=bill_id)
#         serializer = DetailBillSerializer(detail, many=True)
#         response={
#             "data": serializer.data,
#             "status_code": status.HTTP_200_OK,
#         }
#         return Response(response, status=status.HTTP_200_OK)
#     def post(self, request):
#         datas = request.data['data']
#         for data in datas:
#             food_id = data['food_id']
#             bill_id = data['bill_id']
#             amount_billdetail = data['amount']
#             bildetail = DetailBillModel.objects.raw(f"SELECT * FROM order_detailbillmodel WHERE food_id_id = {food_id} AND bill_id_id = {bill_id}")
#             if bildetail:
#                 with connection.cursor() as cursor:
#                     cursor.execute(f"UPDATE order_detailbillmodel SET amount = {amount_billdetail} WHERE food_id_id={food_id} AND bill_id_id={bill_id}")
#             else:
#                 with connection.cursor() as cursor:
#                     cursor.execute(f"INSERT INTO order_detailbillmodel(amount, price, bill_id_id, food_id_id) VALUES({amount_billdetail}, (SELECT food_price FROM food_table_manager_foodmodel WHERE id =  {food_id}), {bill_id},  {food_id})")
#         response = {
#             "message": "Insert success",
#             "status_code": status.HTTP_200_OK
#         }
#         return Response(response, status=status.HTTP_200_OK)

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

# class GetListBillView(APIView):

#     def get(self, request):
#         listbill = DatabaseListBill.objects.raw("""SELECT B.id AS bill_id, SUM(amount) AS amount, SUM(amount*price) AS total 
#             FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F 
#             WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id and B.status=False 
#             GROUP BY B.id""")
#         serializer = ListBillSerializer(listbill, many=True)
#         response = {
#             "data": serializer.data,
#             "status_code": status.HTTP_200_OK
#         }
#         return Response(response, status=status.HTTP_200_OK)

class PrintBillView(APIView):
    
    def get(self, request, pk):
        bill_bill = BillId.objects.raw(f"""SELECT B.id AS bill_id, B.time_created AS time_created, Ta.name AS table_name FROM order_billmodel AS B, food_table_manager_tablemodel AS Ta
                WHERE B.table_id_id = Ta.id AND  table_id_id = {pk}
                AND B.status=false""")
        billSerializer = BillIdSerializer(bill_bill, many=True)
        bill = PrintBill.objects.raw(f"""SELECT B.id AS "bill_id", TB.name AS "table_name"
            , B.time_created AS "time_created" , F.food_name AS "food_name"
            , BD.amount AS "amount", BD.price AS "price"
            , (BD.amount*BD.price) AS "total_price"
            FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F, food_table_manager_tablemodel TB
            WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id AND TB.id = B.table_id_id AND B.status = false AND B.id = (SELECT id AS bill_id FROM order_billmodel 
                WHERE table_id_id = {pk} 
                AND status=false)""")
        serializer = PrintBillSerializer(bill, many=True)
        total1 = SumMoneyBill.objects.raw(f"select sum(price*amount)  from order_billmodel B, order_detailbillmodel DB where DB.bill_id_id=B.id and B.id={pk}")
        serializertotal = SumMoneyBillSerializer(total1)
        a = billSerializer.data[0]
        response = {
            "bill_id": a['bill_id'],
            "time_created": a['time_created'],
            "table_name":a['table_name'],
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

# class SumBill(APIView):
#     def get(self, request, pk):
#         # total1 = SumMoneyBill.objects.raw(f'select 1 as "id_sum", sum(price*amount) as "total"  from order_billmodel B, order_detailbillmodel DB where DB.bill_id_id=B.id and B.id={pk}')
#         # print(total1, "AAA")
#         # serializer = SumMoneyBillSerializer(total1)
#         # print(serializer.data, "AAA")
#         # response = {
#         #     "data": serializer.data,
#         #     "status_code": status.HTTP_200_OK
#         # }
#         # return Response(response, status=status.HTTP_200_OK)
#         total1=DetailBillModel.objects.filter(bill_id=pk)
#         serializer=DetailBillSerializer(total1, many=True)
#         sum=0
#         for data in serializer.data:
#             # print(type(sum), type(data['price']), "AAA")
#             sum+=data['amount']*int(data['price'])
#         response = {
#             "sum": sum,
#             "status_code": status.HTTP_200_OK
#         }
#         return Response(response, status=status.HTTP_200_OK)
# Số món ăn bàn đó gọi
class GetOrderedView(APIView):
    def get(self, request, pk):
        order_food_name = GetFoodOrdered.objects.raw(f"""SELECT D.food_id_id as id, F.food_name AS food_name, f.food_price AS food_price, D.amount AS amount
        FROM order_detailbillmodel AS D, food_table_manager_foodmodel AS F, order_billmodel as B 	
        WHERE D.food_id_id = F.id AND D.bill_id_id=B.id and B.status=False and B.table_id_id={pk}""")
        serializer = GetFoodOrderedSerializer(order_food_name, many=True)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class OrderFoodView(APIView):
    def post(self, request):
        table_id = request.data['table_id']
        # #user_name = request.data['user_name']
        user_id = request.user.id
        foods = request.data['list_food']
        for food in foods:
            print("bichchi")
        if not foods:
            return Response({"message": "Bạn chưa chọn bàn", "status_code": 400}, status=200)
        #user_id['id'] = User.objects.raw(f"""SELECT id FROM authentication_user WHERE username ='{user_name}'""")
        bill_bill = BillId.objects.raw(f"""SELECT id AS bill_id FROM order_billmodel 
            WHERE table_id_id = {table_id} 
            AND status=false""")
        billSerializer = BillaSerializer(bill_bill, many=True)
        a = billSerializer.data[0]
        bill_id = a['bill_id']
        if not bill_id:
            bill = BillModel(table_id=table_id, user_id=user_id)
            bill.save()
            bill_id = DetailBillModel.objects.raw(f"""SELECT id AS bill_id FROM order_billmodel 
                WHERE table_id_id = f{table_id} 
                AND status=false""")
            billSerializer = BillIdSerializer(bill_bill, many=True)
            a = billSerializer.data[0]
            bill_id = a['bill_id']
            cursor.execute(f"""UPDATE food_table_manager_tablemodel SET status = 'Có người' WHERE id = {table_id}""")
        if bill_id:
            foods = request.data['list_food']
            for food in foods:
                food_name = food['food_name']
                food_amount = food['food_amount']
                

                # food_food = GetFoodId.objects.raw(f"""SELECT id AS food_id 
                #     FROM food_table_manager_foodmodel 
                #     WHERE food_name = '{food_name}'""")
                # food_serializer = GetFoodIdSerializer(food_food, many=True)
                # b = food_serializer.data[0]
                # food_id = b['food_id']
                food_id = 1

                check_food_name1 = GetDem.objects.raw(f"""SELECT COUNT(*) AS dem FROM order_detailbillmodel AS D, 
                order_billmodel AS B, food_table_manager_foodmodel AS F
                    WHERE D.bill_id_id = B.id AND F.id = D.food_id_id AND B.id = {bill_id} AND F.food_name = '{food_name}'""")
                c = GetDemSerializer(check_food_name1, many=True)
                # cd = c[0]
                # check_food_name = cd['dem']
                print(c)


                # if check_food_name:
                #     with connection.cursor() as cursor:
                #         cursor.execute(f"""UPDATE order_detailbillmodel 
                #             SET amount = {food_amount} 
                #             WHERE food_id_id={food_id} AND bill_id_id={bill_id}""")    
                # else:
                #     with connection.cursor() as cursor:
                #         cursor.execute(f"""INSERT INTO order_detailbillmodel(amount, price, bill_id_id, food_id_id) 
                #             VALUES({food_amount}, (SELECT food_price FROM food_table_manager_foodmodel WHERE id =  {food_id}), {bill_id},  {food_id})""")
        response = {
            
            "message": "success",
            "status_code": 200
        }
        return Response(response, status=200)