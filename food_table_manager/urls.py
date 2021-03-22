from django.urls import path
from . import views
urlpatterns=[
    path('create_category/', views.CreateCategoriesView.as_view(), name='create_category'),
    path('list_category/', views.getCategoriesView.as_view(), name='get_category'),
    path('detail_category/<int:pk>', views.UpdateCategoriesView.as_view(), name='detail_category'),
    path('search_category/', views.SearchCagoriesView.as_view(), name='search_category'),
    path('create_food/', views.CreateFoodView.as_view(), name='create_food'),
    path('list_food/', views.getFoodView.as_view(), name='list_food'),
    path('list_table/', views.getTableView.as_view(), name='list_table'),
    path('create_table/', views.CreateTableView.as_view(), name='create_table'),
    path('detail_table/<int:pk>', views.UpdateTableView.as_view(), name='detail_table'),
    path('search_table/', views.SearchTableView.as_view(), name='search_table'),
    path('detail_food/<int:pk>', views.UpdateFoodView.as_view(), name='detail_food'),
    path('create_detailfood/', views.CreateDetailFoodView.as_view(), name='create_detailfood'),
    path('get_detailfood/<int:pk>', views.getDetailFoodView.as_view(), name='get_detailfood'),
    path('detail_detailfood/<int:pk>', views.UpdateDetailFooView.as_view(), name='detail_detailfood'),
]