from django.urls import path
from . import views

urlpatterns = [
    path('',views.nestedSerializer),
    path('getbooks/',views.getBooks),
    path('getcategory/',views.getCategory),
]