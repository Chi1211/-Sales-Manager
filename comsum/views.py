from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from .models import LossModel, getLossModel, ConsumptionModel, SaveConsumption, WareHouse, StatisticalModel, ConsumpFoodModel
from .serializers import SaveConsumptionSerializer, WareHouseSerializer, LossModelSerializer, LossSerializer, StatisticalSerializer, ConsumpFoodSerializer
# Create your views here.
class ConsumptionView(APIView):
    def post(self, request):
        con=SaveConsumption.objects.raw("""select material_id, sum(DF.amount_material*BD.amount) as "sum_material"
            from food_table_manager_detailfoodmodel DF,
            (select food_id_id, sum(BD.amount) as "amount"
            from order_billmodel B, order_detailbillmodel BD
            where BD.bill_id_id=B.id and time_created::date=current_date
            group by BD.food_id_id) BD where BD.food_id_id=DF.food_id group by material_id""")
        serializer=SaveConsumptionSerializer(con, many=True)
        consump=ConsumptionModel.objects.raw("""select * from comsum_consumptionmodel where time_consumption::date=current_date""")
        if consump: 
            for data in serializer.data:
                with connection.cursor() as cursor:
                    cursor.execute(f"update comsum_consumptionmodel set amount_consumption={data['sum_material']} where material_id={data['material_id']}")
        else: 
            for data in serializer.data:
                with connection.cursor() as cursor:
                    cursor.execute(f"insert into comsum_consumptionmodel(amount_consumption, time_consumption, material_id) values ({data['sum_material']}, current_date, {data['material_id']})")
        response = {
            "success": "success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

# class LossView(APIView):
#     def post(self, request):
#         con=getLossModel.objects.raw("""select N.material_id_id as "material_id",(coalesce(N.nhap , 0)-coalesce(L.bloss , 0)-coalesce( Ti.tieuthu , 0)-coalesce(Co.material_reality , 0)) as "loss"
# from (select material_id_id, sum(amount) as "nhap" from material_importmaterialmodel group by material_id_id) N
# Left JOIN  (select material_id, sum(amount_loss) as "bloss" from comsum_lossmodel group by material_id) L on N.material_id_id=L.material_id
# Left JOIN  (select material_id, sum(amount_consumption) as "tieuthu" from comsum_consumptionmodel group by material_id) Ti on N.material_id_id=Ti.material_id
# Left join comsum_warehouse Co on Co.id=N.material_id_id""")
#         serializer=LossSerializer(con, many=True)
#         for data in serializer.data:
#             with connection.cursor() as cursor:
#                     cursor.execute(f"insert into comsum_lossmodel(amount_loss, time, material_id) values({data['loss']}, current_date, {data['material_id']})")
#         response = {
#             "success": "success",
#             "status_code": status.HTTP_200_OK
#         }
#         return Response(response, status=status.HTTP_200_OK)

class InsertWareHouse(APIView):
    def post(self, request):
        # save ware
        datas = request.data['data']
        for data in datas:
            material=data['material']
            material_reality=data['material_reality']
            ware=WareHouse.objects.raw(f"select * from comsum_warehouse where material_id={material}")
            if ware: 
                with connection.cursor() as cursor:
                    cursor.execute(f"update comsum_warehouse set material_reality={material_reality}, created=current_date where material_id={material}")
            else: 
                with connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO comsum_warehouse(material_reality, created, material_id) VALUES({material_reality}, current_date,{material})")

        # consumption material_loss
        con=getLossModel.objects.raw("""select N.material_id_id as "material_id",(coalesce(N.nhap , 0)-coalesce(L.bloss , 0)-coalesce( Ti.tieuthu , 0)-coalesce(Co.material_reality , 0)) as "loss"
    from (select material_id_id, sum(amount) as "nhap" from material_importmaterialmodel group by material_id_id) N
    Left JOIN  (select material_id, sum(amount_loss) as "bloss" from comsum_lossmodel group by material_id) L on N.material_id_id=L.material_id
    Left JOIN  (select material_id, sum(amount_consumption) as "tieuthu" from comsum_consumptionmodel group by material_id) Ti on N.material_id_id=Ti.material_id
    Left join comsum_warehouse Co on Co.id=N.material_id_id""")
        serializer=LossSerializer(con, many=True)
        for data in serializer.data:
            with connection.cursor() as cursor:
                    cursor.execute(f"insert into comsum_lossmodel(amount_loss, time, material_id) values({data['loss']}, current_date, {data['material_id']})")
        response={
           'success':"success",
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class StatisticalView(APIView):
    def get(self, request):
        statis= StatisticalModel.objects.raw("""select N.material_id_id as "material_id", Ma.material_name as "material_name",(coalesce(N.nhap , 0)-coalesce(L.bloss , 0)-coalesce(Ti.tieuthu , 0)) as "material_digital", Co.material_reality as "material_reality"
    from (select material_id_id, sum(amount) as "nhap" from material_importmaterialmodel group by material_id_id) N
    Left JOIN  (select material_id, sum(amount_loss) as "bloss" from comsum_lossmodel group by material_id) L on N.material_id_id=L.material_id
    Left JOIN  (select material_id, sum(amount_consumption) as "tieuthu" from comsum_consumptionmodel group by material_id) Ti on N.material_id_id=Ti.material_id
    Left join comsum_warehouse Co on Co.id=N.material_id_id
    inner join material_materialmodel Ma on N.material_id_id=Ma.id""")
        serializer=StatisticalSerializer(statis, many=True)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class ConsumpFood(APIView):
    def post(self, request):
        todate=request.data["todate"]
        fromdate=request.data["fromdate"]
        food=ConsumpFoodModel.objects.raw(f"""select F.id as "food_id", F.food_name, F.food_price
            from food_table_manager_foodmodel F, 
            (select BD.food_id_id as "food_id", sum(BD.amount) as "amount"
            from order_billmodel B, order_detailbillmodel BD
            where BD.bill_id_id=B.id and time_created::date<('{todate}'::date+'1 day'::interval) and time_created::date>='{fromdate}'
            group by BD.food_id_id) B
            where B.food_id=F.id
            ORDER BY B.amount DESC
            LIMIT 10 """)
        serializer=ConsumpFoodSerializer(food, many=True)
        response = {
            "data": serializer.data,
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)
