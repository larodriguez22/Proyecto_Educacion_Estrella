from ..models import Reserva

def get_variables(var_pk):
    reservas = Reserva.objects.filter(pk=var_pk)
    return reservas


def get_muchas():
    reservas = Reserva.objects.all()
    return reservas


def get_reservas(id):

    print(id)
    #reserva = Reserva.objects.raw('SELECT * FROM reservas_reserva WHERE id = %s;', int(id))
   
    try:
        reserva = Reserva.objects.raw("SELECT * FROM reservas_reserva WHERE id = '%s'" % id)[0]
        print(reserva)
        return (reserva)

    except:
        return False

