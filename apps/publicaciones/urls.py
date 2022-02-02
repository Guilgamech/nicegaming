from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inicio, name='index'),
    path('Gaming/', views.listGaming, name='gaming'),
    path('Twitch/', views.listTwitch, name='twitch'),
    path('E-Sport/', views.listEsport, name='esport'),
    path('International/', views.listInternational, name='international'),
    path('Contacto/', views.contactUs, name= 'formContact'),
    path('Contacto/msgContact', views.msgContact, name='msgcontact'),
    path('Suscribirse', views.suscribirse, name='suscribirse'),
    path('Publicaciones/<int:id>/',views.detallePost, name = 'detallePost'),
]