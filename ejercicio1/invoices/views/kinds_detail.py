# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Json
import json

# Modules
from invoices.modules import kind_detail

@csrf_exempt 
def index(request):
    return HttpResponse("Hola! Tipos detalles.")


@csrf_exempt 
def altaTipoDetalle(request):
    """Da de alta un tipo detalle con el dato: name"""

    if request.method == 'POST':
        # Asegura que el método sea POST

        # Para trabajar con el body (postman)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Guarda los datos que vienen en el request
        name = body['name']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que registra al tipo_detalle en la bd, y retorna un mensaje con el resultado obtenido
        message = kind_detail.alta(name)

        return HttpResponse(message)


@csrf_exempt 
def bajaTipoDetalle(request):
    """Da de baja un tipo detalle mediante su id"""

    if request.method == 'DELETE':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina al tipo_detalle de la bd, y retorna un mensaje con el resultado obtenido
        message = kind_detail.baja(id)

        return HttpResponse(message)


@csrf_exempt 
def modificaTipoDetalle(request):
    """Modifica datos (tipodetalle solo tiene name) de un tipo detalle mediante su id"""

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        id = body['id']
        name = body['name']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que modifica al tipo_detalle de la bd, y retorna un mensaje con el resultado obtenido
        message = kind_detail.modifica(id, name)

        return HttpResponse(message)