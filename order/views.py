from django.shortcuts import render
from .models import BillModel
from .serializers import BillSerializer
from rest_framework.views import APIView
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

class CreateDetailBillView(APIView):
    def post(self, request):
        bill_id=request.data['bill_id']
        food_id=request.data['food_id']
        amount=request.data['amount']
        with connection.cursor() as cursor:
            cursor.execute("update order_billmodel set status="+status1+" where id="+str(pk))