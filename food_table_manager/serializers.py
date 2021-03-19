from rest_framework import serializers
from .models import CategoriesModel, FoodModel, GetFoodModel, TableModel, BookTableModel

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoriesModel
        fields='__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodModel
        fields='__all__'

class GetFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetFoodModel
        fields='__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=TableModel
        fields='__all__'

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookTableModel
        fields='__all__'