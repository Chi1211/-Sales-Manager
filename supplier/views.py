from django.shortcuts import render
from .models import SupplierModel
from .serializer import SupplierSerialier
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class getSupplierView(APIView):
    def get(self, request):
        supplier=SupplierModel.objects.all()
        serializer = SupplierSerialier(supplier, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateSupplierView(APIView):
    # permission_classes=(IsAuthenticated,IsAdminUser, )
    def get(self, request):
        supplier=SupplierModel.objects.all()
        serializer = SupplierSerialier(supplier, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=SupplierSerialier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)
        
class UpdateSupplierView(APIView):
    # permission_classes=(IsAuthenticated,IsAdminUser, )
    def get_object(self, pk):
        try: 
            supplier=SupplierModel.objects.get(pk=pk)
            return supplier
        except SupplierModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        supplier=self.get_object(pk)
        serializer=SupplierSerialier(supplier)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        supplier=self.get_object(pk)
        serializer=SupplierSerialier(supplier, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class SearchSupplierView(APIView):
    # permission_classes=(IsAuthenticated,IsAdminUser, )
    def post(self, request):
        name=request.data["supplier_name"]
        supplier=SupplierModel.objects.filter(supplier_name__icontains=name)
        serializer = SupplierSerialier(supplier, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

        