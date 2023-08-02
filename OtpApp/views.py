from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

# Register user
class RegisterUser(APIView):
    def post(self, request):
        try:
            serialized_data = UserSerializer(data = request.data)
            if not serialized_data.is_valid():
                return Response({'status': 404, 'errors': serialized_data.errors})
            
            serialized_data.save()
            return Response({'status': 200,'message':'An otp sent on your email'})
        
        except Exception as e:
            print(e)
            Response({'status': 400, 'exception':e})
    
        
    # verify otp sent on phone number
    # right now no otp is sent on phone number 
    # we are just seeing the otp from database and verifying it
    def patch(self, request):
        try:
            if User.objects.filter(phone=request.data['phone']).exists():
                print("maja aa gaya")
                print(request.data['otp'])
                user = User.objects.get(phone=request.data['phone'])
                saved_otp = user.otp   # get the otp from the database 

                if saved_otp == str(request.data['otp']):    # compare otp of user and database
                    user.is_phone_verified = True
                    user.save()
                    return Response({'status': 200, 'message': 'Okay! phone verified'})
                else:
                    return Response({'status': 403, 'message': 'wrong otp'})
            else:
                return Response({'status': 404, "message": "enter a valid phone no"})

        except Exception as e:
            return Response({'status': 404, 'message': 'Something went wrong'})
        
