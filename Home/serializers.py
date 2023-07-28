from rest_framework import serializers
from .models import Students
from rest_framework.response import Response
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        '''
        we will send all the row to this class and 
        then decide which columns we have to send as response
        it also called making fields serilizable the fields which are not serialized 
        are not sent with the response
        '''
        # exclude = ['phone_no']
        # fields = ['name','phone_no']
        fields = '__all__'

    """
    validate is a predefined function and it has two parameters one is self 
    and another is attrs we can change the name of attrs to what we like.
    And this attrs is a dictionary of data passed by user 
    """
    def validate(self, attrs):
        if 'phone_no' in attrs:
            phone_no_length = len(str(attrs["phone_no"]))
            if phone_no_length != 10:
                # this will stop the flow of program and not let the user save data to database
                raise serializers.ValidationError({'error','enter a valid 10 digit phone no.'})
            
        if 'name' in attrs:
            for i in attrs['name']:
                if i.isdigit():
                    # if there's no error simply return the attrs
                    raise serializers.ValidationError({'error','Name should only contain the aplhabets'})
            
        return attrs


        
    
    