from django.urls import path
from .views import *

urlpatterns = [
    path('create/',RegisterUser.as_view()),
    path('regenerate-otp/', regenerate_otp)
]