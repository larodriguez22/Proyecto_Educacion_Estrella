from ..models import Reserva

def get_variables(var_pk):
    variables = Reserva.objects.filter(pk=var_pk)
    return variables


def get_muchas():
    variables = Reserva.objects.all()
    return variables