from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from.serializer import *

# Create your views here.

def nestedSerializer(request):
    return HttpResponse("Hi it's me Kanha")


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serilized_data = BookSerializer(books,many=True)
    return Response({'status': 200, 'payload': serilized_data.data})


# it is now only show the category as only category field is passed in CategorySerilizer
@api_view(['GET'])
def getCategory(request):
    category = Category.objects.all()
    serilized_data = CategorySerializer(category,many=True)
    return Response({'status': 200, 'payload': serilized_data.data})