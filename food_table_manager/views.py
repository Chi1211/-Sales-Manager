from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriesModel, FoodModel, GetFoodModel, TableModel, BookTableModel
from .serializers import CategoriesSerializer, FoodSerializer, GetFoodSerializer, TableSerializer, BookTableSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.
class getCategoriesView(APIView):
    def get(self, request):
        categories=CategoriesModel.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateCategoriesView(APIView):
    permission_classes=(IsAuthenticated,IsAdminUser, )
    def post(self, request):
        serializer=CategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateCategoriesView(APIView):
    permission_classes=(IsAuthenticated, IsAdminUser)
    def get_object(self, pk):
        try: 
            categories=CategoriesModel.objects.get(pk=pk)
            return categories
        except CategoriesModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        categories=self.get_object(pk)
        serializer=CategoriesSerializer(categories)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        categories=self.get_object(pk)
        serializer=CategoriesSerializer(categories, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class SearchCagoriesView(APIView):
    def get(self, request):
        name=request.data["category_name"]
        categories=CategoriesModel.objects.filter(category_name__contains=name)
        serializer = CategoriesSerializer(categories, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

        
class getFoodView(APIView):
    def get(self, request):
        food=GetFoodModel.objects.raw("select F.id, F.food_name, F.food_price, F.food_image, Ca.category_name from food_table_manager_foodmodel F  inner join food_table_manager_categoriesmodel Ca on F.category_id=Ca.id")
        serializer = GetFoodSerializer(food, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateFoodView(APIView):
    
    def post(self, request):
        serializer=FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class getTableView(APIView):
    def get(self, request):
        table=TableModel.objects.all()
        serializer = TableSerializer(table, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateTableView(APIView):
    
    def post(self, request):
        serializer=TableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateTableView(APIView):
    def get_object(self, pk):
        try: 
            table=TableModel.objects.get(pk=pk)
            return table
        except TableModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        table=self.get_object(pk)
        serializer=TableSerializer(table)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        table=self.get_object(pk)
        serializer=TableSerializer(table, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class SearchTableView(APIView):
    def get(self, request):
        statuss=request.data["status"]
        table=TableModel.objects.filter(status=statuss)
        serializer = TableSerializer(table, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

   
