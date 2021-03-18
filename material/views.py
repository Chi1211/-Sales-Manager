from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MaterialSerializer, ImportMaterialSerializer, GetImportMaterialSerializer
from .models import  MaterialModel, ImportMaterialModel, GetImportMaterialModel
# Create your views here.
class getMaterialView(APIView):
    def get(self, request):
        material=MaterialModel.objects.all()
        serializer = MaterialSerializer(material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
        
class CreateMaterialView(APIView):
    def get(self, request):
        material=MaterialModel.objects.all()
        serializer = MaterialSerializer(material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=MaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateMaterialView(APIView):
    def get_object(self, pk):
        try: 
            material=MaterialModel.objects.get(pk=pk)
            return material
        except MaterialModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        material=self.get_object(pk)
        serializer=MaterialSerializer(material)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        material=self.get_object(pk)
        serializer=MaterialSerializer(material, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)   

class SearchMaterialView(APIView):
    def get(self, request):
        name=request.data["material_name"]
        material=MaterialModel.objects.filter(material_name__contains=name)
        serializer = MaterialSerializer(material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)


class getImportMaterialView(APIView):
    def get(self, request):
        import_material=GetImportMaterialModel.objects.raw('select I.id, Ma.material_name, S.supplier_name, I.amount, I.price, I.import_date from material_importmaterialmodel I inner join material_materialmodel Ma on Ma.id=I.id inner join supplier_suppliermodel S on S.id=I.id')
        serializer = GetImportMaterialSerializer(import_material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
        
class CreateImportMaterialView(APIView):
    def get(self, request):
        import_material=ImportMaterialModel.objects.all()
        serializer = ImportMaterialSerializer(import_material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        serializer=ImportMaterialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class SearchImportMaterialNameView(APIView):
    def get(self, request):
        name=request.data["material_name"]
        
        import_material=GetImportMaterialModel.objects.raw("select I.id, Ma.material_name, S.supplier_name, I.amount, I.price, I.import_date from material_importmaterialmodel I inner join material_materialmodel Ma on Ma.id=I.id inner join supplier_suppliermodel S on S.id=I.id where Ma.material_name like '%%"+name+"%%'")
        serializer = GetImportMaterialSerializer(import_material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class SearchImportMaterialDateView(APIView):
    def get(self, request):
        from_date=request.data["from_date"]
        to_date=request.data["to_date"]
        import_material=GetImportMaterialModel.objects.raw("select I.id, Ma.material_name, S.supplier_name, I.amount, I.price, I.import_date from material_importmaterialmodel I inner join material_materialmodel Ma on Ma.id=I.id inner join supplier_suppliermodel S on S.id=I.id where I.import_date BETWEEN '"+ from_date +"' AND '"+to_date+"'")
        serializer = GetImportMaterialSerializer(import_material, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)



