from django.contrib import admin
from .models import Charla, Reserva


@admin.register(Charla)
class CharlaAdmin(admin.ModelAdmin):
    pass


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass
