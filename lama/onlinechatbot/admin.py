from django.contrib import admin
from .models import Exhibit, Event, Ticket, Feedback

# Register your models here.

admin.site.register(Exhibit)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Feedback)


