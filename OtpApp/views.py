from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer

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
    
        