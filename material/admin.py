from django.contrib import admin
from .models import MaterialModel, ImportMaterialModel
# Register your models here.

admin.site.register(MaterialModel)
admin.site.register(ImportMaterialModel)