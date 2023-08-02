from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone','password']

    # this function is only because to save save the password in hash format 
    # otherwise if save the serialized object data then also it will create user in db
    def create(self, validated_data):
        user = User.objects.create(email= validated_data['email'], phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        user.save()
        return user