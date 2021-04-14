from django.urls import path
from . import views
urlpatterns=[
    path('create_category/', views.CreateCategoriesView.as_view()),
    path('list_category/', views.getCategoriesView.as_view()),
    path('detail_category/<int:pk>', views.UpdateCategoriesView.as_view()),
    path('search_category/', views.SearchCategoriesView.as_view()),
    path('create_food/', views.CreateFoodView.as_view()),
    path('list_food/', views.getFoodView.as_view()),
    path('list_category_food/<str:category>', views.getCategoryFoodView.as_view()),
    path('list_table/', views.getTableView.as_view()),
    path('create_table/', views.CreateTableView.as_view()),
    path('detail_table/<int:pk>', views.UpdateTableView.as_view()),
    path('search_table/<str:statuss>', views.SearchTableView.as_view()),
    path('detail_food/<int:pk>', views.UpdateFoodView.as_view()),
    path('create_detailfood/', views.CreateDetailFoodView.as_view()),
    path('get_detailfood/<int:pk>', views.getDetailFoodView.as_view()),
    path('delete_detailfood/<int:pk>', views.UpdateDetailFoodView.as_view()),
    path('book_table/', views.BookTableView.as_view()),
    path('update_book_table/<int:pk>', views.UpdateBookTableView.as_view()),
    path('cancel_book_table/<int:pk>', views.CancelBookTableView.as_view()),
  
]