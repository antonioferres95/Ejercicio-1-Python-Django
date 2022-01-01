from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import KindDetail

@csrf_exempt 
def index(request):
    return HttpResponse("Módulo Tipo Detalle")


def verificaExistencia(id2):
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
    if (verificaExistencia(id2)):
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
    if(verificaExistencia(id2)):
        kd = KindDetail.objects.get(id=id2)
        kd.name = name
        kd.save()
        return HttpResponse("El tipo detalle cuyo id es {} ha sido modificado en la bd satisfactoriamente".format(id2))
    else:
        return HttpResponse("No existe ningun tipo detalle cuyo id sea: {}".format(id2))
    
