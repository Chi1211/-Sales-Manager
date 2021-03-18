from django.urls import path
from . import views
urlpatterns=[
    path('list_supplier/', views.CreateSupplierView.as_view(), name="list_supplier"),
    path('detail_supplier/<int:pk>', views.UpdateSupplierView.as_view(), name="detail_supplier"),
    path('search_supplier/', views.SearchSupplierView.as_view(), name="search_supplier"),
    path('get_supplier/', views.getSupplierView.as_view(), name="get_supplier"),
]