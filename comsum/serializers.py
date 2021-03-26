from rest_framework import serializers
from .models import SaveConsumption, WareHouse, getLossModel, LossModel, StatisticalModel
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