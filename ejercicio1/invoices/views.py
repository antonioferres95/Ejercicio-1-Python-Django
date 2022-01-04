from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Invoice
from .models import KindDetail
from .models import Client

@csrf_exempt 
def index(request):
    return HttpResponse("Hola!")


def verificaExistencia(id2):
    # Verifica la existencia de una factura mediante su id
    if Invoice.objects.filter(id=id2).exists():
        return True
    else:
        return False
    
  
@csrf_exempt 
def altaFactura(request):
    # Da de alta una factura con el dato: number (date se carga automaticamente al cargar la factura)

    # Para trabajar con el body (postman)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    # Guarda los datos que vienen en el request
    number = body['number']
    cuit2 = body['cuit']

    # Verifica que exista un cliente con dicho cuit, instancia la clase Invoice, y registra los datos en la bd
    if (Client.objects.filter(cuit=cuit2).exists()):
        fac = Invoice()
        fac.client = Client.objects.get(cuit=cuit2)
        fac.number = number
        fac.save()

        return HttpResponse("Los datos number:{} y date: {} han sido guardados satisfactoriamente para el cliente con cuit {}"
        .format(number, fac.date.strftime('%d %b %Y - %H:%M hrs'), cuit2))
    else:
        return HttpResponse("No existe ningun cliente cuyo cuit sea: {}. No fue posible añadir la factura.".format(cuit2))
    
    
@csrf_exempt 
def bajaFactura(request):
    # Dar de baja una factura mediante su id

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id2 = body['id']

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica su existencia y luego lo elimina de la bd
    if (verificaExistencia(id2)):
        fac = Invoice.objects.get(id=id2)
        fac.delete()
        return HttpResponse("La factura cuyo id es {} ha sido eliminada de la bd satisfactoriamente".format(id2))
    else: 
        return HttpResponse("No existe ninguna factura cuyo id sea: {}".format(id2))



@csrf_exempt 
def modificaFactura(request):
    # Modificar datos de una factura mediante su id

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    id2 = body['id']
    number = body['number']
    date = body['date']

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo modifica en la bd
    if(verificaExistencia(id2)):
        fac = Invoice.objects.get(id=id2)
        fac.number = number
        fac.date = date
        fac.save()
        return HttpResponse("La factura cuyo id es {} ha sido modificada en la bd satisfactoriamente".format(id2))
    else: 
        return HttpResponse("No existe ninguna factura cuyo id sea: {}".format(id2))
    

def verificaExistencia2(id2):
    # Verifica la existencia de un tipo detalle mediante su id
    if KindDetail.objects.filter(id=id2).exists():
        return True
    else:
        return False


@csrf_exempt 
def altaTipoDetalle(request):
    # Da de alta un tipo detalle con el dato: name

    # Para trabajar con el body (postman)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    # Guarda los datos que vienen en el request
    name = body['name']

    # Instancia la clase KindDetail, y registra los datos en la bd
    kd = KindDetail()
    kd.name = name
    kd.save()

    return HttpResponse("El dato name:{} ha sido guardado satisfactoriamente".format(name))


@csrf_exempt 
def bajaTipoDetalle(request):
    # Dar de baja un tipo detalle mediante su id

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    id2 = body['id']

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo elimina de la bd
    if (verificaExistencia2(id2)):
        kd = KindDetail.objects.get(id=id2)
        kd.delete()
        return HttpResponse("El tipo detalle cuyo id es {} ha sido eliminado de la bd satisfactoriamente".format(id2))
    else: 
        return HttpResponse("No existe ningun tipo detalle cuyo id sea: {}".format(id2))



@csrf_exempt 
def modificaTipoDetalle(request):
    # Modificar datos (tipodetalle solo tiene name) de un tipo detalle mediante su id

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    id2 = body['id']
    name = body['name']

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo modifica en la bd
    if(verificaExistencia2(id2)):
        kd = KindDetail.objects.get(id=id2)
        kd.name = name
        kd.save()
        return HttpResponse("El tipo detalle cuyo id es {} ha sido modificado en la bd satisfactoriamente".format(id2))
    else:
        return HttpResponse("No existe ningun tipo detalle cuyo id sea: {}".format(id2))
    

def verificaExistencia3(cuit2):
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
    
    if not verificaExistencia3(cuit2):
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
    if (verificaExistencia3(cuit2)):
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
    if (verificaExistencia3(cuit2)):
        cli = Client.objects.get(cuit=cuit2)
        cli.name = name
        cli.clienteCode = clientCode
        cli.save()
        return HttpResponse("El cliente cuyo cuit es {} ha sido modificado en la bd satisfactoriamente".format(cuit2))
    else: 
        return HttpResponse("No existe ningun cliente cuyo cuit sea: {}".format(cuit2))
