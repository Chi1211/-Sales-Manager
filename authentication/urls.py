from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('checktoken/', views.CheckToken.as_view(), name="checktoken"),
    path('change_pass/', views.ChangePasswordView.as_view(), name='change_pass'),
    path('change_profile/<str:username>', views.ChangeProfileView.as_view(), name='change_profile'),
    path('list_user/', views.UserView.as_view(), name='list_user'),
    path('update_user/<str:username>', views.UpdateUserView.as_view(), name='update_user'),
]   