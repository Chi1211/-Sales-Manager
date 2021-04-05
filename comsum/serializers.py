from rest_framework import serializers
from .models import SaveConsumption, WareHouse, getLossModel, LossModel, StatisticalModel, ConsumpFoodModel, GetStatistics, General, GetWareHouse, DateOfWare
class SaveConsumptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model=SaveConsumption
        fields='__all__'

class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=WareHouse
        fields='__all__'

class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model=getLossModel
        fields='__all__'
        
class LossModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LossModel
        fields='__all__'

class StatisticalSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatisticalModel
        fields='__all__'

class ConsumpFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConsumpFoodModel
        fields='__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetStatistics
        fields = '__all__'
        
class GeneralaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = '__all__'

class GetWareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetWareHouse
        fields = '__all__'

        
class DateOfWareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateOfWare
        fields = '__all__'