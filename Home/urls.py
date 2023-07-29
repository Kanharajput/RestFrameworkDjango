from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # it will handle all the requests
    path('',StudentGetPost.as_view()),
    path('upd-del/<id>/',StudentUpdateDelete.as_view()),
    path('register-user/',views.generateToken),

]