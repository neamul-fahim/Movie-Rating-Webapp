from django.urls import path
from . import views

urlpatterns = [
    path('signup-page/', views.SignupView.as_view(), name='signupPage'),
    path('', views.LoginView.as_view(), name='loginPage'),
    path('signup-API/', views.SignupAPIView.as_view(), name='signupAPI'),
    path('login-API/', views.LoginAPIView.as_view(), name='loginAPI'),
    path('get_user/', views.UserProfileAPIView.as_view(), name='getUser'),

]
