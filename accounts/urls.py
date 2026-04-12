from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView 

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view())
]