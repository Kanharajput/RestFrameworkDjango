from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# now this will only accept the get request
# using @api_view decorator now it won't remain the same view method
# GET describe here that it only accept the GET request from GET,POST,PUT,PATCH and DELETE
@api_view(['GET'])
def home(request):
    return Response({'first-name: kanha', "second-name:tomar"})

