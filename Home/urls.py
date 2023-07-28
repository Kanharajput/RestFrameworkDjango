from django.urls import path
from .views import StudentApi
from . import views

urlpatterns = [
    # it will handle all the requests
    path('',StudentApi.as_view()),
    path('register-user/',views.generateToken),
]