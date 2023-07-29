from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# get the savepdf method from helper class
from .helpers import savePdf
from .faker import generateRandomData

# we can 
@api_view(['GET'])
def generatePdf(request):
    # also we can get the data from model
    students = generateRandomData()
    params = {
        'students' : students
    }

    file_name, status = savePdf(params)

    if not status: 
        return Response({'status': 500, 'message': 'something went wrong'})
    
    else:
        return Response({'status': 200, 'path': f'/media/{file_name}.pdf'})
