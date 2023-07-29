from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings

# type of arguement is dict
def savePdf(params: dict):
    template = get_template('Home/index.html')       
    html = template.render(params)                   # render the dict
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)
    file_name = uuid.uuid4()        # generate a random file name

    try: 
        with open(str(settings.BASE_DIR) + f'/Media/{file_name}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)

    except Exception as e:
        print(e)    

    
    if pdf.err:
        return '', False
    
    else:
        return file_name, True