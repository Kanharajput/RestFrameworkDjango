from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer, UserSerializer
from .models import Students
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# imports to make StudentApi Token Authorization
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# to generate jwt token for a new user
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# generate jwt tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def generateToken(request):
    user_serialized = UserSerializer(data = request.data)
    if not user_serialized.is_valid():
        return Response({'status' : 400, 'message': 'please enter a valid user data','errors': user_serialized.errors})
    
    user_serialized.save()
    user = User.objects.get(username=user_serialized.data['username'])
    tokens = get_tokens_for_user(user)
    return Response({'status': 200, 
                     'payload': 'token created', 
                     'refresh': str(tokens['refresh']),
                     'access':str(tokens['access'])
                    })
  

# Class based View
# using just one url we can handle all the request
class StudentApi(APIView):
    # authenticate via jwt token
    # user has to pass the access token in the bearer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)    # print the user who is accessing this data
        students =  Students.objects.all()
        serialized_students = StudentSerializer(students, many=True)
        return Response({'status': 200,'payload': serialized_students.data})  
    
    def post(self, request):
        student = request.data
        serialized_student = StudentSerializer(data=request.data) # we mut it in kwargs format

        if serialized_student.is_valid():
            serialized_student.save()
            return Response({'status': 200, 'payload': student, 'message': 'Student data added successfully'})
        
        return Response({'status': 200, 'error': serialized_student.errors})

    def put(self, request):
        try:
            student_id = request.data['id']
            student = Students.objects.get(id=student_id)
            serializer_data = StudentSerializer(student, data=request.data)
            if not serializer_data.is_valid():
                return Response({'status':403 ,'errors': serializer_data.errors})
            
            serializer_data.save()
            return Response({'status':200, 'payload': serializer_data.data,'message': 'student data is updated'})

        except Exception as e:
            print(e)
            return Response({'status' : 403,'error' : 'invalid id'})


    def patch(self, request):
        try:
            student_id = request.data['id']
            student = Students.objects.get(id=student_id)
            serializer_data = StudentSerializer(student, data=request.data, partial=True)
            if not serializer_data.is_valid():
                return Response({'status':403 ,'errors': serializer_data.errors})
        
            serializer_data.save()
            return Response({'status':200, 'payload': serializer_data.data,'message': 'student data is updated'})

        except Exception as e:
            print(e)
            return Response({'status' : 403,'error' : 'invalid id'})      

    def delete(self, request):
        try:
            # pass id in url like 8000/?id=28
            id = request.GET.get('id')
            student = Students.objects.get(id=id)
            student.delete()
            return Response({'status': 200, 'payload': 'student data deleted succesfully'})
 
        except Exception as e:
            print(e)
            return Response({'status': 400, 'error': 'may be wrong id'})


'''
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
 
# PUT
# so if we want to update the data using put then we have to write the values for the fields also which we are not going to update
# otherwise it won't work. But we can left the fields which are default and auto incrementing like id.

# PATCH
# patch is better than put if we have to update only selected fields. To enable patch just add partial=True 
# in serializer class constructor. no need to change the decorator.

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
    

@api_view(['DELETE'])
def deleteData(request):
    try:
        # if url is delete-db/?id=23 then we have to get the id like this
        id = request.GET.get('id')
        student = Students.objects.get(id=id)
        student.delete()
        return Response({'status': 200, 'payload': 'student data deleted succesfully'})
 
    except Exception as e:
        print(e)
        return Response({'status': 400, 'error': 'may be wrong id'})
'''