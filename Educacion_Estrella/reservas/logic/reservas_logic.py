from ..models import Reserva

def get_variables(var_pk):
    reservas = Reserva.objects.filter(pk=var_pk)
    return reservas


def get_muchas():
    reservas = Reserva.objects.all()
    return reservas



"""
def get_reservas(nombre):

    reserva =Reserva.objects.get(pk=nombre)
    #reserva = Reserva.objects.raw('SELECT * FROM reservas_reserva WHERE id=%s' % ids)[0]
    return reserva
"""

def get_reservas(id):

    print(id)
    #reserva = Reserva.objects.raw('SELECT * FROM reservas_reserva WHERE id = %s;', int(id))
   


    try:
        reserva = Reserva.objects.raw("SELECT * FROM reservas_reserva WHERE id = '%s'" % id)[0]
        print(reserva)
        return (reserva)

    except:
        return False


    #UPDATE reservas_reserva SET estudiante='maria';--


"""
def get_reservas(request):
    if request.is_ajax():
        search_term = request.POST.get('searchTerm')

        # Searching employees using Django ORM - the best way
        employees = Employee.objects.filter(mentor__icontains=search_term)

        #Searching employees using raw() - the correct way
        reservas = Reserva.objects.raw('SELECT * FROM Reserva WHERE first_name ILIKE %s;',[search_term])

        return reservas

"""

