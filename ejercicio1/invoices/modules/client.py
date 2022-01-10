# Models
from invoices.models.clients import Client

def verificaExistencia(cuit2):
    """Verifica la existencia de un cliente mediante su cuit"""
    if Client.objects.filter(cuit=cuit2).exists():
        return True
    else:
        return False


def alta(cuit2, name, clientCode):
    """Da de alta un cliente con los datos: cuit, name y cliente code"""

    if not verificaExistencia(cuit2):
    # Si no existe un cliente con este cuit, instancia la clase Client, y registra los datos en la bd
        try:
            cli = Client()
            cli.cuit = cuit2
            cli.name = name
            cli.clientCode = clientCode
            cli.save()
            return ("Los datos name:{} cuit:{} y código cliente:{} han sido almacenados satisfactoriamente.".format(
                name, cuit2, clientCode))
        except:
            return ("Ocurrió un error inesperado. No fue posible registrar los datos en la base de datos.")
    else:
        return ("El cliente con cuit:{} ya se encuentra registrado.".format(cuit2))


def baja(cuit2):
    """Da de baja un cliente mediante su cuit"""
    
    # Obtiene la instancia cuyo cuit sea igual al solicitado, verifica que exista y luego lo elimina de la bd     
    if (verificaExistencia(cuit2)):
        try:
            cli = Client.objects.get(cuit=cuit2)
            cli.delete()
            return ("El cliente cuyo cuit es {} ha sido eliminado de la base de datos satisfactoriamente.".format(cuit2))
        except:
             return ("Ocurrió un error inesperado. No fue posible eliminar los datos de la base de datos.")
    else: 
        return ("No existe ningun cliente cuyo cuit sea: {}.".format(cuit2))


def modifica(cuit2, name, clientCode):
    """Modifica datos de un cliente mediante su cuit (suponiendo que solo puede cambiarse el name y el clientCode)"""

    # Obtiene la instancia cuyo cuit sea igual al solicitado, verifica que exista y luego lo modifica 
    if (verificaExistencia(cuit2)):
        try:
            cli = Client.objects.get(cuit=cuit2)
            cli.name = name
            cli.clientCode = clientCode
            cli.save()
            return ("El cliente cuyo cuit es {} ha sido modificado en la base de datos satisfactoriamente.".format(cuit2))
        except:
            return ("Ocurrió un error inesperado. No fue posible modificar los datos de la base de datos.")
    else: 
        return ("No existe ningun cliente cuyo cuit sea: {}.".format(cuit2))