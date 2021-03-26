from django.contrib import admin
from .models import BillModel,  DetailBillModel, DatabaseListBill, PrintBill
# Register your models here.
admin.site.register(BillModel)

admin.site.register(DetailBillModel)
admin.site.register(DatabaseListBill)