from django.db import models
from food_table_manager.models import TableModel
from authentication.models import User
from food_table_manager.models import FoodModel
from material.models import MaterialModel

# Create your models here.
class BillModel(models.Model):
    table_id=models.ForeignKey(TableModel, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    name_customer=models.CharField(max_length=255, default="")
    phone_customer=models.CharField(max_length=255, default="")
    time_created=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    
class DetailBillModel(models.Model):
    bill_id=models.ForeignKey(BillModel, on_delete=models.CASCADE)
    food_id=models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    amount=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=19, decimal_places=0)

class DatabaseListBill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    total = models.IntegerField()

class PrintBill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    time_created = models.DateTimeField()
    food_name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    total_price = models.IntegerField()
    
class SumMoneyBill(models.Model):
    sum=models.IntegerField(primary_key=True)

class ConsumptionModel(models.Model):
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    amount_consumption=models.IntegerField()
    # amount_consumption_lost=models.IntegerField(default=0)
    time_consumption=models.DateField()

class SaveConsumption(models.Model):
    material_id=models.IntegerField(primary_key=True)
    sum_material=models.IntegerField()

class WareHouse(models.Model):
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    material_digital=models.IntegerField(default=0)
    material_reality=models.IntegerField(default=material_digital)

class LossModel(models.Model):
    mater=models.IntegerField()
    material_loss=models.IntegerField()
    time_update=models.DateField(auto_now=True)