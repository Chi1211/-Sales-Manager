from django.db import models
from material.models import MaterialModel

# Create your models here.
class CategoriesModel(models.Model):
    category_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name

class FoodModel(models.Model):
    food_name=models. CharField(max_length=255)
    food_price=models.IntegerField()
    category=models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    food_image=models.ImageField(upload_to='food/', null=True, blank=True)

class GetFoodModel(models.Model):
    id=models.IntegerField(primary_key=True)
    food_name=models. CharField(max_length=255)
    food_price=models.IntegerField()
    food_image=models.ImageField(upload_to='food/', null=True, blank=True)
    category_name=models.CharField(max_length=255)

class TableModel(models.Model):
    name=models.CharField(max_length=255, default="")
    status=models.CharField(max_length=255, choices=[('Có người', 'Có người'), ("Trống", "Trống"), ("Tạm ngưng hoạt động", "Tạm ngưng hoạt động"),  ("Bàn đã đặt", "Bàn đã đặt")], default="Trống")

class BookTableModel(models.Model):
    table=models.ForeignKey(TableModel, on_delete=models.CASCADE)
    time_book=models.DateTimeField()
    name_book=models.CharField(max_length=255)
    phone_book=models.CharField(max_length=15)
    number_of_people=models.IntegerField()
    money_book=models.IntegerField()

class DetailFoodModel(models.Model):
    food= models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    material=models.ForeignKey(MaterialModel, on_delete=models.CASCADE)
    amount_material=models.IntegerField(default=1)

class getDetailFoodModel(models.Model):
    id=models.IntegerField(primary_key=True)
    material_name=models.CharField(max_length=255)
    amount_material=models.IntegerField(default=1)



