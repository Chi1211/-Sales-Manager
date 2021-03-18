from .models import SupplierModel
from rest_framework import serializers
class SupplierSerialier(serializers.ModelSerializer):
    class Meta:
        model=SupplierModel
        fields='__all__'
