from django.views.generic import CreateView
from .models import Reserva
from .forms import ReservaForm


class CrearReserva(CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = '/'
