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