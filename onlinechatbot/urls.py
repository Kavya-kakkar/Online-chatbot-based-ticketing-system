from django.urls import path , include

from accounts.views import register , logout 

from . import views

urlpatterns = [
    path('',views.index,name='index'), 
    path('About/',views.About,name='About'),
    path('event/',views.event,name='event'),
    path('exhibit/',views.exhibit,name='exhibit'),
    path('login/',views.login,name='login'),
    path('time/',views.time,name='time'),
    path('accounts/',include('accounts.urls')),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('our_terms/',views.our_terms,name='our_terms'),
    path('carrer/',views.carrer,name='carrer'),
    path('mission/',views.mission,name='mission'),
    path('partnerships/',views.partnerships,name='partnerships'),
    path('FAQ/',views.FAQ,name='FAQ'),
    path('booking_guide/',views.booking_guide,name='booking_guide'),
    path('Cacellation/',views.Cacellation,name='Cacellation'),
    path('site_map/',views.site_map,name='site_map'),
    path('Newsletter/',views.Newsletter,name='Newsletter'),
    path('Blog/',views.Blog,name='Blog'),
    path('Gallery/',views.Gallery,name='Gallery'),
    path('Offers/',views.Offers,name='Offers'),
    path('Privacy/',views.Privacy,name='Privacy'),
    
]