from django.urls import path
from .views import UserRegister, UserLoginView

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name="login")
]
