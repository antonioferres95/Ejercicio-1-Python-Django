# Models
from invoices.models.kinds_detail import KindDetail


def verificaExistencia(id2):
    """Verifica la existencia de un tipo detalle mediante su id"""
    if KindDetail.objects.filter(id=id2).exists():
        return True
    else:
        return False


def alta(name):
    """Da de alta un tipo detalle con el dato: name"""

    # Instancia la clase KindDetail, y registra los datos en la bd
    try:
        td = KindDetail()
        td.name = name
        td.save()
        return ("El dato name:{} ha sido almacenado en la base de datos satisfactoriamente.".format(name))
    except:
        return ("Ocurrió un error inesperado. No fue posible registrar los datos en la base de datos.")


def baja(id2):
    """Da de baja un tipo detalle mediante su id"""

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo elimina de la bd
    if (verificaExistencia(id2)):
        try:
            td = KindDetail.objects.get(id=id2)
            td.delete()
            return ("El tipo detalle cuyo id es {} ha sido eliminado de la base de datos satisfactoriamente.".format(id2))
        except:
            return ("Ocurrió un error inesperado. No fue posible eliminar los datos de la base de datos.")
    else: 
        return ("No existe ningun tipo detalle cuyo id sea: {}.".format(id2))


def modifica(id2, name):
    """Modifica datos (tipodetalle solo tiene name) de un tipo detalle mediante su id"""

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo modifica en la bd
    if(verificaExistencia(id2)):
        try:
            td = KindDetail.objects.get(id=id2)
            td.name = name
            td.save()
            return ("El tipo detalle cuyo id es {} ha sido modificado en la base de datos satisfactoriamente.".format(id2))
        except:
            return ("Ocurrió un error inesperado. No fue posible modificar los datos de la base de datos.")
    else:
        return ("No existe ningun tipo detalle cuyo id sea: {}.".format(id2))