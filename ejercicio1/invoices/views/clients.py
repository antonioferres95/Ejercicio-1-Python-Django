# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Json
import json

# Modules
from invoices.modules import client

@csrf_exempt 
def index(request):
    return HttpResponse("Hola! Clientes.")


@csrf_exempt 
def altaCliente(request):
    """Da de alta un cliente con los datos: cuit, name y cliente code"""

    if request.method == 'POST':
        # Asegura que el método sea POST

        # Para trabajar con el body (postman)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Guarda los datos que vienen en el request
        cuit = body['cuit']
        name = body['name']
        clientCode = body['clientCode']
        
        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que registra al cliente en la bd, y retorna un mensaje con el resultado obtenido
        message = client.alta(cuit, name, clientCode)

        return HttpResponse(message)


@csrf_exempt 
def bajaCliente(request):
    """Da de baja un cliente mediante su cuit"""

    if request.method == 'DELETE':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        cuit = body['cuit']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina al cliente de la bd, y retorna un mensaje con el resultado obtenido
        message = client.baja(cuit)

        return HttpResponse(message)


@csrf_exempt 
def modificaCliente(request):
    """Modifica datos de un cliente mediante su cuit (suponiendo que solo puede cambiarse el name y el clientCode)"""

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        cuit = body['cuit']
        name = body['name']
        clientCode = body['clientCode']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que modifica al cliente en la bd, y retorna un mensaje con el resultado obtenido
        message = client.modifica(cuit, name, clientCode)

        return HttpResponse(message)