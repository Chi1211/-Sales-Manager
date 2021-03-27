from .models import BillModel, DetailBillModel, DatabaseListBill, PrintBill, SumMoneyBill
from comsum.models import getLossModel
from rest_framework import serializers
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillModel
        fields='__all__'

class DetailBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailBillModel
        fields='__all__'

class ListBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=DatabaseListBill
        fields='__all__'

class PrintBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrintBill
        fields='__all__'

class SumMoneyBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=SumMoneyBill
        fields='__all__'

