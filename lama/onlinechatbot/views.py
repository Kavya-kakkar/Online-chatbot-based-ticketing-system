from django.shortcuts import render
from .models import Exhibit, Event, Ticket, Feedback


def index(request):
    return render(request,"index.html", )

def About(request):
    return render(request,"About.html")

def event(request):
    events = Event.objects.all()
    return render(request,"event.html" , {'events' : events})

def exhibit(request):
    exhibits = Exhibit.objects.all()
    return render(request,"exhibit.html" , {'exhibits' : exhibits})

def login(request):
    return render(request,"login.html")

def time(request):
    return render(request,"time.html")
