from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # only show the category field 
        fields = ['category']


class BookSerializer(serializers.ModelSerializer):
    # this will show the category data which is related to this Book
    category = CategorySerializer()
    class Meta: 
        model = Book
        fields = '__all__'