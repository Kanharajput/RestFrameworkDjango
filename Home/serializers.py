from rest_framework import serializers
from .models import Students

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