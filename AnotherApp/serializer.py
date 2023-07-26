from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # only show the category field 
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # this will show the name of category when get the call from getBook and it will not interfair when call is by getCategory. Category is now independent and it can return all it's field
    # and it is not nested serializer now
    category = serializers.ReadOnlyField(source="category.category")
    class Meta: 
        model = Book
        fields = '__all__'
