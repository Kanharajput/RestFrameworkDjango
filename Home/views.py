from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Students

# now this will only accept the get request
# using @api_view decorator now it won't remain the same view method
# GET describe here that it only accept the GET request from GET,POST,PUT,PATCH and DELETE
@api_view(['GET'])
def provideFromDB(request):
    students = Students.objects.all()   
    serializer_data = StudentSerializer(students, many=True)           # set many=True if more than one enteries in students
    return Response({'status': 200,'payload': serializer_data.data})

@api_view(['POST'])
def saveToDB(request):  
    data = request.data
    print(data)
    return Response({'status':200,'payload':data})