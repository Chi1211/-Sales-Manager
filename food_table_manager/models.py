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
    status=models.CharField(max_length=255, choices=[('Có người', 'Có người'), ("Trống", "Trống"), ("Tạm ngưng hoạt động", "Tạm ngưng hoạt động")], default="Trống")
    person=models.IntegerField()

    # def __str__(self):
    #     return self.id

class BookTableModel(models.Model):
    table=models.ForeignKey(TableModel, on_delete=models.CASCADE)
    time_book=models.DateTimeField(auto_now=True)
    name_book=models.CharField(max_length=255)
    phone_book=models.CharField(max_length=15)
    number_of_people=models.IntegerField()
    money_book=models.DecimalField(max_digits=19,  decimal_places=2)
