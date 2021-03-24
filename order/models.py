from django.db import models
from food_table_manager.models import TableModel
from authentication.models import User
from food_table_manager.models import FoodModel

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