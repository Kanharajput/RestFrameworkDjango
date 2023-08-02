from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User
from .helpers import send_otp_to_mobile
from rest_framework.decorators import api_view

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
        

@api_view(['PATCH'])
def regenerate_otp(request):
    try:
        is_user = User.objects.filter(phone = request.data['phone']).exists()
        if is_user:
            user = User.objects.get(phone = request.data['phone'])
            sent_or_not = send_otp_to_mobile(user, request.data['phone'])

            if sent_or_not:
                return Response({'status': 200, 'message': 'Otp sent'})
            
            else: 
                return Response({'status': 500, 'message': f'try after sometime'})

    except Exception as e:
        print(e)
        return Response({'status': 400, 'message': 'something went wrong'})