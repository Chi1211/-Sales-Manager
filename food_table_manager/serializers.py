from rest_framework import serializers
from .models import CategoriesModel, FoodModel, GetFoodModel, TableModel, BookTableModel, DetailFoodModel, getDetailFoodModel

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoriesModel
        fields='__all__'
        ordering = ['category_name']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodModel
        fields='__all__'

class GetFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetFoodModel
        fields='__all__'
        ordering = ['food_name']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableModel
        fields='__all__'

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookTableModel
        fields='__all__'

class DetailFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailFoodModel
        fields=['material', 'amount_material']

class getDetailFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=getDetailFoodModel
        fields='__all__'
