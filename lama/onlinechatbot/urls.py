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

]