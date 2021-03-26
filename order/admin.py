from django.contrib import admin
from .models import BillModel, ConsumptionModel, DetailBillModel, DatabaseListBill, PrintBill
# Register your models here.
admin.site.register(BillModel)
admin.site.register(ConsumptionModel)
admin.site.register(DetailBillModel)
admin.site.register(DatabaseListBill)