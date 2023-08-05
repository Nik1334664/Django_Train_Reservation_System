from django.contrib import admin
from .models import Reservation, Cabin, Seat

admin.site.register(Reservation)
admin.site.register(Cabin)
admin.site.register(Seat)
