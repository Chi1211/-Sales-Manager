from django.urls import path
from . import views
urlpatterns=[
    path('list_material/', views.CreateMaterialView.as_view(), name="list_material"),
    path('detail_material/<int:pk>', views.UpdateMaterialView.as_view(), name="detail_material"),
    path('search_material/', views.SearchMaterialView.as_view(), name="search_material"),
    path('get_material/', views.getMaterialView.as_view(), name="get_material"),
    path('get_importmaterial/', views.getImportMaterialView.as_view(), name="get_material"),
    path('list_importmaterial/', views.CreateImportMaterialView.as_view(), name="list_material"),
    path('search_name_importmaterial/', views.SearchImportMaterialNameView.as_view(), name="search_name_importmaterial"),
    path('search_date_importmaterial/', views.SearchImportMaterialDateView.as_view(), name="search_date_importmaterial"),
]