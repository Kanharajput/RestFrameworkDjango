from django.urls import path
from . import views
urlpatterns = [
    # pdf generate path
    path('',views.generatePdf),
]