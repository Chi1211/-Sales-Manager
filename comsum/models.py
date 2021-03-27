from django.db import models
from material.models import MaterialModel
# Create your models here.
class LossModel(models.Model):
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    amount_loss=models.IntegerField()
    time=models.DateField(auto_now=True)

class getLossModel(models.Model):
    material_id=models.IntegerField(primary_key=True)
    loss=models.IntegerField()

class ConsumptionModel(models.Model):
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    amount_consumption=models.IntegerField()
    time_consumption=models.DateField()

class SaveConsumption(models.Model):
    material_id=models.IntegerField(primary_key=True)
    sum_material=models.IntegerField()

class WareHouse(models.Model):
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    material_reality=models.IntegerField(default=0)
    created=models.DateField(auto_now=True)

class StatisticalModel(models.Model):
    material_id=models.IntegerField(primary_key=True, default=0)
    material_name=models.CharField(max_length=255)
    material_digital=models.IntegerField()
    material_reality=models.IntegerField()
