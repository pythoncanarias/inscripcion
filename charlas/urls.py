from django.conf.urls import url
from .views import CrearReserva

urlpatterns = [
    url(r'^$', CrearReserva.as_view()),
]
