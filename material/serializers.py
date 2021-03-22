from rest_framework import serializers
from .models import MaterialModel, ImportMaterialModel, GetImportMaterialModel


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialModel
        fields='__all__'
        ordering = ['material_name', 'pk']

class ImportMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImportMaterialModel
        fields='__all__'
        ordering = ['import_date']

class GetImportMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetImportMaterialModel
        fields='__all__'
        ordering = ['import_date']
