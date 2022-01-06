# Models
from invoices.models import Invoice, Client


def verificaExistencia(id2):
    # Verifica la existencia de una factura mediante su id
    if Invoice.objects.filter(id=id2).exists():
        return True
    else:
        return False


def alta(number, cuit2):
    # Da de alta una factura con el dato: number (date se carga automaticamente al cargar la factura)

    # Verifica que exista un cliente con dicho cuit, instancia la clase Invoice, y registra los datos en la bd
    if (Client.objects.filter(cuit=cuit2).exists()):
        try:
            fac = Invoice()
            fac.client = Client.objects.get(cuit=cuit2)
            fac.number = number
            fac.save()
            return ("Los datos number:{} y date: {} de la factura han sido guardados satisfactoriamente para el cliente con cuit {}."
            .format(number, fac.date.strftime('%d %b %Y - %H:%M hrs'), cuit2))
        except:
             return ("Ocurrió un error inesperado. No fue posible registrar los datos en la base de datos.")
    else:
        return ("No existe ningun cliente cuyo cuit sea: {}. No fue posible almacenar la factura.".format(cuit2))


def baja(id2):
    # Da de baja una factura mediante su id

    # Obtiene la instancia cuyo id sea igual al solicitado, verifica su existencia y luego lo elimina de la bd
    if (verificaExistencia(id2)):
        try:
            fac = Invoice.objects.get(id=id2)
            fac.delete()
            return ("La factura cuyo id es {} ha sido eliminada de la base de datos satisfactoriamente.".format(id2))
        except:
             return ("Ocurrió un error inesperado. No fue posible eliminar los datos de la base de datos.")
    else: 
        return ("No existe ninguna factura cuyo id sea: {}.".format(id2))


def modifica(id2, number, date):
    #Modifica datos de una factura mediante su id

     # Obtiene la instancia cuyo id sea igual al solicitado, verifica que exista y luego lo modifica en la bd
    if(verificaExistencia(id2)):
        try:
            fac = Invoice.objects.get(id=id2)
            fac.number = number
            fac.date = date
            fac.save()
            return ("La factura cuyo id es {} ha sido modificada en la base de datos satisfactoriamente.".format(id2))
        except:
            return ("Ocurrió un error inesperado. No fue posible modificar los datos de la base de datos.")
    else: 
        return ("No existe ninguna factura cuyo id sea: {}.".format(id2))
    