from .models import BillModel, DetailBillModel
from rest_framework import serializers
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillModel
        fields='__all__'

class DetailBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailBillModel
        fields='__all__'