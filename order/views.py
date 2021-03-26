from django.shortcuts import render
from .models import BillModel, DetailBillModel, DatabaseListBill, PrintBill, SumMoneyBill, SaveConsumption
from .serializers import BillSerializer, DetailBillSerializer, ListBillSerializer, PrintBillSerializer, SumMoneyBillSerializer, SaveConsumptionSerializer, LossSerializer
from rest_framework.views import APIView
from comsum.models import getLossModel
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
# Create your views here.
class CreateBillView(APIView):
    def post(self, request):
        serializer=BillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)
class UpdateBillView(APIView):
    def get_object(self, pk):
        try: 
            bill=BillModel.objects.get(pk=pk)
            return bill
        except BillModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        bill=self.get_object(pk)
        serializer=BillSerializer(bill)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)

    # sửa status
    def put(self, request, pk):

        status1=request.data['status']
        with connection.cursor() as cursor:
            cursor.execute("update order_billmodel set status="+status1+" where id="+str(pk))
        bill=self.get_object(pk)
        serializer = BillSerializer(bill)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

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


class InsertBillInfoView(APIView):
    def get(self, request):
        bill_id = request.data['bill_id']
        detail=DetailBillModel.objects.filter(bill_id=bill_id)
        serializer = DetailBillSerializer(detail, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        datas = request.data['data']
        for data in datas:
            food_id = data['food_id']
            bill_id = data['bill_id']
            amount_billdetail = data['amount']
            bildetail = DetailBillModel.objects.raw(f"SELECT * FROM order_detailbillmodel WHERE food_id_id = {food_id} AND bill_id_id = {bill_id}")
            if bildetail:
                with connection.cursor() as cursor:
                    cursor.execute(f"UPDATE order_detailbillmodel SET amount = {amount_billdetail} WHERE food_id_id={food_id} AND bill_id_id={bill_id}")
            else:
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO order_detailbillmodel(amount, price, bill_id_id, food_id_id) VALUES({amount_billdetail}, (SELECT food_price FROM food_table_manager_foodmodel WHERE id =  {food_id}), {bill_id},  {food_id})")
        response = {
            "message": "Insert success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

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

class GetListBillView(APIView):

    def get(self, request):
        listbill = DatabaseListBill.objects.raw("""SELECT B.id AS bill_id, SUM(amount) AS amount, SUM(amount*price) AS total 
            FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F 
            WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id and B.status=False 
            GROUP BY B.id""")
        serializer = ListBillSerializer(listbill, many=True)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class PrintBillView(APIView):
    
    def get(self, request, pk):
        bill = PrintBill.objects.raw(f"""SELECT B.id AS "bill_id", TB.name AS "table_name"
            , B.time_created AS "time_created" , F.food_name AS "food_name"
            , BD.amount AS "amount", BD.price AS "price"
            , (BD.amount*BD.price) AS "total_price"
            FROM order_billmodel B, order_detailbillmodel BD, food_table_manager_foodmodel F, food_table_manager_tablemodel TB
            WHERE B.id = BD.bill_id_id AND BD.food_id_id = F.id AND TB.id = B.table_id_id AND B.status = false AND B.id = {pk}""")
        serializer = PrintBillSerializer(bill, many=True)
        total1 = SumMoneyBill.objects.raw(f"select sum(price*amount)  from order_billmodel B, order_detailbillmodel DB where DB.bill_id_id=B.id and B.id={pk}")
        serializertotal = SumMoneyBillSerializer(total1)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class SumBill(APIView):
    def get(self, request, pk):
        total1 = SumMoneyBill.objects.raw(f"select sum(price*amount)  from order_billmodel B, order_detailbillmodel DB where DB.bill_id_id=B.id and B.id={pk}")
        serializer = SumMoneyBillSerializer(total1)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class ConsumptionView(APIView):
    def post(self, request):
        con=SaveConsumption.objects.raw("""select material_id, DF.amount_material*BD.amount as "sum_material"
                                            from food_table_manager_detailfoodmodel DF,
                                            (select food_id_id, sum(BD.amount) as "amount"
                                            from order_billmodel B, order_detailbillmodel BD
                                            where BD.bill_id_id=B.id and time_created::date=current_date
                                            group by BD.food_id_id) BD where BD.food_id_id=DF.food_id""")

        serializer=SaveConsumptionSerializer(con, many=True)
        for data in serializer.data:
            with connection.cursor() as cursor:
                    cursor.execute(f"insert into order_consumptionmodel(amount_consumption, time_consumption, material_id) values ({data['sum_material']}, current_date, {data['material_id']})")
        response = {
            "success": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class LossView(APIView):
    def post(self, request):
        con=getLossModel.objects.raw("""select material_id as material_id, (material_digital-material_reality) as "loss"
            from order_warehouse""")
        serializer=LossSerializer(con, many=True)
        for data in serializer.data:
            with connection.cursor() as cursor:
                    cursor.execute(f"insert into comsum_lossmodel(amount_loss, time, material_id) values({data['loss']}, current_date, {data['material_id']})")
        response = {
            "success": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class InsertWareHouse(APIView):
    def post(self, request):
        material_realize=request.data['material_reality']
        
        pass