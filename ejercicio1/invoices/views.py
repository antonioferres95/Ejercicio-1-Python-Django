from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Invoice
from clients.models import Client

@csrf_exempt 
def index(request):
    return HttpResponse("Módulo Facturas")


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
    
    


