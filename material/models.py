from django.db import models
from supplier.models import SupplierModel

# Create your models here.


class MaterialModel(models.Model):
    material_name=models.CharField(max_length=255)

    def __str__(self):
        return self.material_name

class ImportMaterialModel(models.Model):
    supplier_id=models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    material_id=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    amount=models.IntegerField()
    price=models.DecimalField(max_digits=19, decimal_places=3)
    import_date=models.DateTimeField()

class GetImportMaterialModel(models.Model):
    id=models.IntegerField(primary_key=True)
    material_name=models.CharField(max_length=255)
    supplier_name=models.CharField(max_length=255)
    amount=models.IntegerField()
    price=models.DecimalField(max_digits=19, decimal_places=10)
    import_date=models.DateTimeField()
    