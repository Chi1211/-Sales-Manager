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
    price=models.IntegerField()

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
    
class SumMoneyBill(models.Model):
    id_sum=models.IntegerField(primary_key=True, default=1)
    total=models.IntegerField(default=0)

class GetFoodOrdered(models.Model):
    id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    food_price = models.IntegerField()


class GetFoodOrdered(models.Model):
    id=models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    food_price = models.IntegerField()

class GetFoodId(models.Model):
    food_id = models.IntegerField(primary_key=True)

class GetAmount(models.Model):
    amount = models.IntegerField(primary_key=True)

class GetDem(models.Model):
    dem = models.IntegerField(primary_key=True)

class BillId(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    time_created = models.DateTimeField()
    table_name = models.CharField(max_length=255)

class getPriceFood(models.Model):
    food_price = models.IntegerField(primary_key=True)


class GetBillInfo(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    time_created = models.DateTimeField()
    total_price = models.IntegerField()

class PrintBill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    time_created = models.DateTimeField()
    food_name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    total_price = models.IntegerField()

class GetFoodId(models.Model):
    food_id = models.IntegerField(primary_key=True)

class GetBillId(models.Model):
    bill_id = models.IntegerField(primary_key=True)

class GetCount(models.Model):
    count = models.IntegerField(primary_key=True)

class SumMoney(models.Model):
    sum_price = models.IntegerField(primary_key=True)