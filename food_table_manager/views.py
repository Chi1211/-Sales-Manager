from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriesModel, FoodModel, GetFoodModel, TableModel, BookTableModel, DetailFoodModel, getDetailFoodModel
from .serializers import CategoriesSerializer, FoodSerializer, GetFoodSerializer, TableSerializer, BookTableSerializer, DetailFoodSerializer, getDetailFoodSerializer
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Max
from django.db import connection
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
    permission_classes=(IsAdminUser,)
    # permission_classes=(IsAuthenticated,IsAdminUser, )
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
    permission_classes=(IsAdminUser,)
    # permission_classes=(IsAuthenticated, IsAdminUser)
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

class SearchCategoriesView(APIView):
    def post(self, request):
        name=request.data["category_name"]
        categories=CategoriesModel.objects.filter(category_name__icontains=name)
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

class getCategoryFoodView(APIView):
    def get(self, request, category):
        food=GetFoodModel.objects.raw(f"""select F.id, F.food_name,  F.food_price, F.food_image from food_table_manager_foodmodel F inner join food_table_manager_categoriesmodel Ca on F.category_id=Ca.id where Ca.category_name='{category}'""")
        serializer = GetFoodSerializer(food, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateFoodView(APIView):
    permission_classes=(IsAdminUser,)
    def post(self, request):
        serializer=FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateFoodView(APIView):
    permission_classes=(IsAdminUser,)
    def get_object(self, pk):
        try: 
            food=FoodModel.objects.get(pk=pk)
            return food
        except FoodModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        food=self.get_object(pk)
        serializer=FoodSerializer(food)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        food=self.get_object(pk)
        serializer=FoodSerializer(food, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class getDetailFoodView(APIView):
    permission_classes=(IsAdminUser,)
    def get(self, request, pk):
        # return Response(food_id, status=status.HTTP_200_OK)
        detail_food=getDetailFoodModel.objects.raw('select D.id, Ma.material_name, D.amount_material from food_table_manager_detailfoodmodel D inner join material_materialmodel Ma on Ma.id=D.material_id inner join food_table_manager_foodmodel F on F.id=D.food_id where D.food_id='+str(pk))
        serializer = getDetailFoodSerializer(detail_food, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            datas = request.data['data']
        except:
            return Response({'errors':'errors'}, status=status.HTTP_400_BAD_REQUEST)
        for data in datas:    
            detail= DetailFoodModel.objects.filter(material=data['material'], food=pk)
            if detail:
                detail.update(amount_material= data['amount_material'])
                # detail_food= DetailFoodModel.objects.update(material=data['material'], food=pk, amount_material= data['amount_material'])               
            else: 
                DetailFoodModel.objects.create(material_id=data['material'], food_id=pk, amount_material= data['amount_material'])
        response={
            "success":"success",
            "status_code": 200
            }
        return Response(response, status=200)

class CreateDetailFoodView(APIView):
    permission_classes=(IsAdminUser,)
    def get(self, request):
        detail_food=getDetailFoodModel.objects.raw('select D.id, Ma.material_name, D.amount_material from food_table_manager_detailfoodmodel D inner join material_materialmodel Ma on Ma.id=D.material_id inner join food_table_manager_foodmodel F on F.id=D.food_id where D.food_id=(select max(id) from food_table_manager_foodmodel)')
        serializer = getDetailFoodSerializer(detail_food, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        data=request.data
        food_id=FoodModel.objects.all().aggregate(Max('id'))
        detail= DetailFoodModel.objects.filter(material=data['material'], food=food_id['id__max'])
        if detail:
            detail.update(amount_material= data['amount_material'])
            # detail_food= DetailFoodModel.objects.update(material=data['material'], food=pk, amount_material= data['amount_material'])               
        else: 
            DetailFoodModel.objects.create(material_id=data['material'], food_id=food_id['id__max'], amount_material= data['amount_material'])
            # print(food_id, "AAA")
        response={
           'success': 'success',
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateDetailFoodView(APIView):
    permission_classes=(IsAdminUser,)
    def get_object(self, pk):
        try: 
            detail_food=DetailFoodModel.objects.get(pk=pk)
            return detail_food
        except DetailFoodModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)

    def delete(self,request,pk):
        detail_food=self.get_object(pk)
        detail_food.delete()
        response={
            'success':"success",
            "status_code": status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class getTableView(APIView):

    def get(self, request):
        table=TableModel.objects.raw("select * from food_table_manager_tablemodel where status <>'T???m ng??ng ho???t ?????ng'")
        serializer = TableSerializer(table, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class CreateTableView(APIView): 
    permission_classes=(IsAdminUser,)  
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
    def get(self, request, statuss):
        table=TableModel.objects.filter(status=statuss)
        serializer = TableSerializer(table, many=True)
        response={
            "data": serializer.data,
            "status_code": status.HTTP_200_OK,
        }
        return Response(response, status=status.HTTP_200_OK)

class BookTableView(APIView):    
    # def get(self, request):
    #     book=BookTableModel.objects.all()
    #     serializer = BookTableSerializer(book, many=True)
    #     response={
    #         "data": serializer.data,
    #         "status_code": status.HTTP_200_OK,
    #     }
    #     return Response(response, status=status.HTTP_200_OK)
    def post(self, request):
        table=request.data['table']
        with connection.cursor() as cursor:
            cursor.execute(f"update food_table_manager_tablemodel set status='B??n ???? ?????t' where id={table}")
        serializer=BookTableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
           'data': serializer.data,
           'status_code': status.HTTP_201_CREATED
        }
        return Response(response, status=status.HTTP_201_CREATED)

class UpdateBookTableView(APIView):
    def get_object(self, pk):
        try: 
            # book=BookTableModel.objects.raw("select id, table_id as table, time_book, name_book, phone_book, number_of_people, money_book from food_table_manager_booktablemodel where id=(select max(id) from food_table_manager_booktablemodel where table_id="+str(pk)+")")
            # print(book, 'AAA')
            book=BookTableModel.objects.filter(table=pk).aggregate(Max('id'))
            if book:

 
                detail_book=BookTableModel.objects.get(pk=book['id__max'])
            
            # detail_book=BookTableModel.objects.get(pk=pk)
                print(book, 'AAA')
                return detail_book
            else: return Response({"errors":"errors"}, status=404)
        except BookTableModel.DoesNotExist:
            return Response({"errors":"errors"}, status=404)
    def get(self, request, pk):
        book=self.get_object(pk)
        serializer=BookTableSerializer(book)
        
        response={
            "data": serializer.data,
            "status_code": 200
        }
        return Response(response, status=200)
    def put(self, renquest, pk):
        book=self.get_object(pk)
        serializer=BookTableSerializer(book, data=renquest.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response={
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class CancelBookTableView(APIView):    
    def post(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(f"update food_table_manager_tablemodel set status='Tr???ng' where id={pk}")
        response={
           'success': "success",
           'status_code': 200
        }
        return Response(response, status=200)
