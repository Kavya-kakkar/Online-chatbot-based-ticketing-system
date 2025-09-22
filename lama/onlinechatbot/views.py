from django.shortcuts import render
from .models import Exhibit, Event, Ticket


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
    time = Ticket.objects.all()
    return render(request,"time.html")

def our_terms(request):
    return render(request,"our_terms.html")

def carrer(request):
    return render(request,"carrer.html")

def mission(request):
    return render(request,"mission.html")

def partnership(request):
    return render(request,"partnership.html")

def FAQ(request):
    return render(request,"FAQ.html")

def booking(request):
    return render(request,"booking.html")

def Cacellation(request):
    return render(request,"Cacellation.html")

def site_map(request):
    return render(request,"site_map.html")

def newletter(request):
    return render(request,"newletter.html")

def Blog(request):
    return render(request,"Blog.html")

def Gallery(request):
    return render(request,"Gallery.html")

def Offers(request):
    return render(request,"Offers.html")

def privacy(request):
    return render(request, "privacy.html")


