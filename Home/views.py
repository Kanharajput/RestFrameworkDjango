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
    data = request.data                # to print the data in payload in Response
    serializer_data = StudentSerializer(data=request.data)        # kwargs parameter
    if not serializer_data.is_valid():
        return Response({'status':403, 'error':serializer_data.errors})
    
    else:
        serializer_data.save()  
        # 200-299 define succussful responses
        # 200 define ok and 201 define created
        return Response({'status':201,'payload':data, 'message':'data saved'})
    
'''
PUT
so if we want to update the data using put then we have to write the values for the fields also which we are not going to update
otherwise it won't work. But we can left the fields which are default and auto incrementing like id.
'''
'''
PATCH
patch is better than put if we have to update only selected fields. To enable patch just add partial=True 
in serializer class constructor. no need to change the decorator.
'''
@api_view(['PUT'])
def updateDB(request, id):
    try:
        # fetching the student data with id
        student = Students.objects.get(id=id)
        # passing student here again to update data so that it won't create a new row
        serializer_data = StudentSerializer(student, data=request.data, partial=True)
        if not serializer_data.is_valid():
            return Response({'status':403 ,'errors': serializer_data.errors})
        
        serializer_data.save()
        return Response({'status':200, 'payload': serializer_data.data,'message': 'student data is updated'})

    except Exception as e:
        print(e)
        return Response({'status' : 403,'error' : 'invalid id'})