from django.urls import path
from .views import (RegisterApi, LoginApi, CekAuth, LogoutApi)
urlpatterns = [
    path('register',RegisterApi.as_view()),
    path('login',LoginApi.as_view()),
    path('checking',CekAuth.as_view()),
    path('logout',LogoutApi.as_view()),
]