from django.contrib import admin
from .models import Exhibit, Event, Ticket

# Register your models here.

admin.site.register(Exhibit)
admin.site.register(Event)
admin.site.register(Ticket)


