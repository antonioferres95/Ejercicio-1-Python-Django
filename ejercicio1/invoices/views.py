# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Json
import json

# Modules
from .modules import kind_detail, client, invoice

@csrf_exempt 
def index(request):
    return HttpResponse("Hola!")


# ---- VISTAS FACTURAS ----
    

@csrf_exempt 
def altaFactura(request):
    # Da de alta una factura con el dato: number (date se carga automaticamente al cargar la factura)

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
    # Da de baja una factura mediante su id

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina la factura de la bd, y retorna un mensaje con el resultado obtenido
        message = invoice.baja(id)

        return HttpResponse(message)


@csrf_exempt 
def modificaFactura(request):
    # Modifica datos de una factura mediante su id

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
       

# ---- VISTAS TIPO DETALLE ----


@csrf_exempt 
def altaTipoDetalle(request):
    # Da de alta un tipo detalle con el dato: name

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
    # Da de baja un tipo detalle mediante su id

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        id = body['id']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina al tipo_detalle de la bd, y retorna un mensaje con el resultado obtenido
        message = kind_detail.baja(id)

        return HttpResponse(message)


@csrf_exempt 
def modificaTipoDetalle(request):
    # Modifica datos (tipodetalle solo tiene name) de un tipo detalle mediante su id

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        id = body['id']
        name = body['name']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que modifica al tipo_detalle de la bd, y retorna un mensaje con el resultado obtenido
        message = kind_detail.modifica(id, name)

        return HttpResponse(message)
 

# ---- VISTAS CLIENTE ----


@csrf_exempt 
def altaCliente(request):
    # Da de alta un cliente con los datos: cuit, name y cliente code

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
    # Da de baja un cliente mediante su cuit

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        cuit = body['cuit']

        # IF JSON CORRECTO (FALTA ESTO)
        # Llama a la función que elimina al cliente de la bd, y retorna un mensaje con el resultado obtenido
        message = client.baja(cuit)

        return HttpResponse(message)


@csrf_exempt 
def modificaCliente(request):
    # Modifica datos de un cliente mediante su cuit (suponiendo que solo puede cambiarse el name y el clientCode)

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

