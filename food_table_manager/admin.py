from django.contrib import admin
from .models import CategoriesModel, FoodModel, TableModel
# Register your models here.
admin.site.register(CategoriesModel)
admin.site.register(FoodModel)
admin.site.register(TableModel)