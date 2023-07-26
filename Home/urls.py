from django.urls import path
from .views import StudentApi

urlpatterns = [
    # it will handle all the requests
    path('',StudentApi.as_view()),
]