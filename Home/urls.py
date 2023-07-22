from django.urls import path
from . import views

urlpatterns = [
    path('',views.provideFromDB),
    path('upload-data/',views.saveToDB),
    path('update-db/<id>/',views.updateDB),
]