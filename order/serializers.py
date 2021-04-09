from .models import GetDem, GetFoodId, BillId, BillModel, DetailBillModel, DatabaseListBill, PrintBill, SumMoneyBill, GetFoodOrdered
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
        fields=['food_name', 'price', 'amount', 'total_price']

class SumMoneyBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=SumMoneyBill
        fields=['id_sum','total']

class GetFoodOrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetFoodOrdered
        fields = '__all__'

class BillIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillId
        fields = '__all__'

class GetFoodIdSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = GetFoodId
        fields = ['food_id']

class GetDemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetDem
        fields = ['dem']

class BillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillId
        fields = ['bill_id']