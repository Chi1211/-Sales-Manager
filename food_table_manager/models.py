from django.db import models

# Create your models here.
class CategoriesModel(models.Model):
    category_name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_name

class FoodModel(models.Model):
    food_name=models. CharField(max_length=255)
    food_price=models.DecimalField(max_digits=19,  decimal_places=2)
    category=models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    food_image=models.ImageField(upload_to='food/', null=True, blank=True)

class GetFoodModel(models.Model):
    id=models.IntegerField(primary_key=True)
    food_name=models. CharField(max_length=255)
    food_price=models.DecimalField(max_digits=19,  decimal_places=2)
    food_image=models.ImageField(upload_to='food/', null=True, blank=True)
    category_name=models.CharField(max_length=255)


class TableModel(models.Model):
    # status=models.CharField(max_length=255, choices=["Có người": 1, "Trống": 2, "Tạm ngưng hoạt động": 3], default="Trống")
    person=models.IntegerField()

