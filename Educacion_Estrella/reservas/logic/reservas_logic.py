from ..models import Reserva

def get_variables(var_pk):
    variables = Variable.objects.filter(pk=var_pk)
    return variables


