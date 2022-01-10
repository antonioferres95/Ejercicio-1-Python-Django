# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Json
import json

# Modules
from invoices.modules import invoice

@csrf_exempt 
def index(request):
    return HttpResponse("Hola! Facturas.")


@csrf_exempt 
def altaFactura(request):
    """Da de alta una factura con el dato: number (date se carga automaticamente al cargar la factura)"""

    if request.method == 'POST':
        # Asegura que el método sea POST

        # Para trabajar con el body (postman)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Guarda los datos que vienen en el request
        number = body['number']
        cuit = body['cuit']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que registra la factura en la bd, y retorna un mensaje con el resultado obtenido
        message = invoice.alta(number, cuit)

        return HttpResponse(message)
        
    
@csrf_exempt 
def bajaFactura(request):
    """Da de baja una factura mediante su id"""

    if request.method == 'DELETE':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina la factura de la bd, y retorna un mensaje con el resultado obtenido
        message = invoice.baja(id)

        return HttpResponse(message)


@csrf_exempt 
def modificaFactura(request):
    """Modifica datos de una factura mediante su id"""

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        id = body['id']
        number = body['number']
        date = body['date']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que modifica la factura en la bd, y retorna un mensaje con el resultado obtenido
        message = invoice.modifica(id, number, date)

        return HttpResponse(message)