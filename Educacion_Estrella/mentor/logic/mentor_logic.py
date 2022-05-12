from ..models import Mentor

def get_todos():
    mentores = Mentor.objects.all()
    return mentores
