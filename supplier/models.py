from django.db import models

# Create your models here.
class SupplierModel(models.Model):
    supplier_name=models.CharField(max_length=255)
    supplier_address=models.CharField(max_length=400, default='')
    supplier_phone=models.CharField(max_length=15)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.supplier_name