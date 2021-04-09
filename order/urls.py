from django.urls import path
from . import views
urlpatterns=[
    # path('create_bill/', views.CreateBillView.as_view()),
    # path('update_bill/<int:pk>', views.UpdateBillView.as_view()),
    path('pay_bill/<int:pk>', views.BillPayView.as_view()),
    # path('update_detail_bill/', views.InsertBillInfoView.as_view()),
    path('switch_table/', views.SwitchTableView.as_view()),
    # path('list_bill/', views.GetListBillView.as_view()),
    path('print_bill/<int:pk>', views.PrintBillView.as_view()),
    # path('sum_bill/<int:pk>', views.SumBill.as_view()),
    #get order
    #path('get_food_ordered/<int:pk>', views.GetOrderedView.as_view()),
    # truyền bàn
    path('food_ordered/', views.OrderFoodView.as_view()),
]