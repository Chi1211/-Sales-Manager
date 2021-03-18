from rest_framework import serializers
from .models import CategoriesModel, FoodModel

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoriesModel
        fields='__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodModel
        fields='__all__'


