from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Client
from invoices.models import Invoice

@csrf_exempt 
def index(request):
    return HttpResponse("Módulo Clientes")


def verificaExistencia(cuit2):
    # Verifica la existencia de un cliente mediante su cuit
    if Client.objects.filter(cuit=cuit2).exists():
        return True
    else:
        return False
    
    
@csrf_exempt 
def altaCliente(request):
    # Da de alta un cliente con los datos: cuit, name y cliente code

    # Para trabajar con el body (postman)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    # Guarda los datos que vienen en el request
    cuit2 = body['cuit']
    name = body['name']
    clientCode = body['clientCode']
    
    if not verificaExistencia(cuit2):
        # Si no existe un cliente con este cuit, instancia la clase Client, y registra los datos en la bd
        cli = Client()
        cli.cuit = cuit2
        cli.name = name
        cli.clienteCode = clientCode
        cli.save()
        return HttpResponse("Los datos name:{} cuit:{} y código cliente:{} han sido guardados satisfactoriamente".format(
            name, cuit2, clientCode))
    else:
        return HttpResponse("El cliente con cuit:{} ya se encuentra registrado.".format(cuit2))


@csrf_exempt 
def bajaCliente(request):
    # Dar de baja un cliente mediante su cuit

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    cuit2 = body['cuit']

    # Obtiene la instancia cuyo cuit sea igual al solicitado, verifica que exista y luego lo elimina de la bd
    if (verificaExistencia(cuit2)):
        cli = Client.objects.get(cuit=cuit2)
        cli.delete()
        return HttpResponse("El cliente cuyo cuit es {} ha sido eliminado de la bd satisfactoriamente".format(cuit2))
    else: 
        return HttpResponse("No existe ningun cliente cuyo cuit sea: {}".format(cuit2))
    


@csrf_exempt 
def modificaCliente(request):
    # Modificar datos de un cliente mediante su cuit (suponiendo que solo puede cambiarse el name y el clientCode)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    cuit2 = body['cuit']
    name = body['name']
    clientCode = body['clientCode']

    # Obtiene la instancia cuyo cuit sea igual al solicitado, verifica que exista y luego lo modifica 
    if (verificaExistencia(cuit2)):
        cli = Client.objects.get(cuit=cuit2)
        cli.name = name
        cli.clienteCode = clientCode
        cli.save()
        return HttpResponse("El cliente cuyo cuit es {} ha sido modificado en la bd satisfactoriamente".format(cuit2))
    else: 
        return HttpResponse("No existe ningun cliente cuyo cuit sea: {}".format(cuit2))


    


