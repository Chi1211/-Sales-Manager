from django.urls import path
from . import views
urlpatterns=[
# Truyền đối số table_id vào ô tham số pk
    # Thanh toán
    path('pay_bill/<int:pk>', views.BillPayView.as_view()),
    # Chuyển bàn
    path('switch_table/', views.SwitchTableView.as_view()),
    # In hóa đơn
    path('print_bill/<int:pk>', views.PrintBillView.as_view()),
    # In list món ăn bàn đó đã gọi
    path('food_ordered/<int:pk>', views.GetOrderedView.as_view()),
    # Gọi món ăn(Tạo bill gọi món)
    path('order_food/', views.OrderFoodView.as_view())
]