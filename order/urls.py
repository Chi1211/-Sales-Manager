from django.urls import path
from . import views
urlpatterns=[
    path('create_bill/', views.CreateBillView.as_view()),
    path('update_bill/<int:pk>', views.UpdateBillView.as_view())
]