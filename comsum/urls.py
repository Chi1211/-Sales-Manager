from django.urls import path
from . import views
urlpatterns=[
    path('consumption/', views.ConsumptionView.as_view()),
    path('statis/', views.StatisticalView.as_view()),
    path('check_ware/', views.InsertWareHouse.as_view()),
    path('load_date_ware/', views.DateOfWareView.as_view()),
    path('consum_food/', views.ConsumpFood.as_view()),
    path('statis_month/', views.StatisticsMonthView.as_view()),
    path('general/', views.GeneralaaView.as_view()),
    path('chart_product/', views.ChartProductView.as_view())




]
