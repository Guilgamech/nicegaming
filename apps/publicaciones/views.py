import form as form
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.http import JsonResponse
from django.views.generic import ListView
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.views.generic import View
from django.core.paginator import Paginator
from django.core import serializers
from .models import Categoria, Informacion, Post, RedesSociales, Suscripcion
import random
from .forms import contactoForm
from .utils import *


# Create your views here.


def Inicio(request, *args, **kwargs):
    posts = list(Post.objects.filter(
        estado=True,
        publicado=True
    ).values_list('id', flat=True))

    aleatoriPost = random.choice(posts)
    posts.remove(aleatoriPost)
    principal = consulta(aleatoriPost)

    post1 = random.choice(posts)
    posts.remove(post1)

    post2 = random.choice(posts)
    posts.remove(post2)

    post3 = random.choice(posts)
    posts.remove(post3)

    post4 = random.choice(posts)
    posts.remove(post4)

    try:
        post_gaming = Post.objects.filter(
            estado=True,
            publicado=True,
            Categoria=Categoria.objects.get(nombre='Gaming')
        ).latest('fecha_publicacion')
    except:
        post_gaming = None

    response = {
        'aleatoriPost': principal,
        'post1': consulta(post1),
        'post2': consulta(post2),
        'post3': consulta(post3),
        'post4': consulta(post4),
        'postGaming': post_gaming,
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
    }
    return render(request, 'index.html', response)


def listGaming(request, *args, **kwargs):
    post_gaming = Post.objects.filter(
        estado=True,
        publicado=True,
        Categoria=Categoria.objects.get(nombre='Gaming')
    )
    try:
        categoria = Categoria.objects.get(nombre='Gaming')

    except:
        categoria = None

    paginacion = Paginator(post_gaming, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    response = {
        'posts': posts,
        'postGaming': post_gaming,
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
        'categoria': categoria,
    }

    return render(request, 'Categoria/listCategoria.html', response)


def listTwitch(request, *args, **kwargs):
    post_twitch = Post.objects.filter(
        estado=True,
        publicado=True,
        Categoria=Categoria.objects.get(nombre='Twitch')
    )
    try:
        categoria = Categoria.objects.get(nombre='Twitch')

    except:
        categoria = None

    paginacion = Paginator(post_twitch, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    response = {
        'posts': posts,
        'postTwitch': post_twitch,
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
        'categoria': categoria,
    }

    return render(request, 'Categoria/listCategoria.html', response)


def listEsport(request, *args, **kwargs):
    post_esport = Post.objects.filter(
        estado=True,
        publicado=True,
        Categoria=Categoria.objects.get(nombre='E-Sport')
    )
    try:
        categoria = Categoria.objects.get(nombre='E-Sport')

    except:
        categoria = None

    paginacion = Paginator(post_esport, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    response = {
        'posts': posts,
        'postEsport': post_esport,
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
        'categoria': categoria,
    }

    return render(request, 'Categoria/listCategoria.html', response)


def listInternational(request, *args, **kwargs):
    post_international = Post.objects.filter(
        estado=True,
        publicado=True,
        Categoria=Categoria.objects.get(nombre='International')
    )
    try:
        categoria = Categoria.objects.get(nombre='International')

    except:
        categoria = None

    paginacion = Paginator(post_international, 3)
    pagina = request.GET.get('page')
    posts = paginacion.get_page(pagina)

    response = {
        'posts': posts,
        'postInternational': post_international,
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
        'categoria': categoria,
    }

    return render(request, 'Categoria/listCategoria.html', response)


def contactUs(request, *args, **kwargs):
    form = contactoForm

    response = {
        'socialLinks': obtenerRedes,
        'informacion': obtenerInformacion,
        'form': form,
    }

    return render(request, 'Contacto/contacto.html', response)


def msgContact(request, *args, **kwargs):
    formulario = contactoForm(data=request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        response[form] = formulario

    return redirect('/Contacto/')


def detallePost(request, id, *args, **kwargs):
    try:
        postShow = Post.objects.get(id=id)
    except:
        postShow = None
    posts = list(Post.objects.filter(
        estado=True,
        publicado=True
    ).values_list('id', flat=True))
    posts.remove(postShow.id)
    post1 = random.choice(posts)
    posts.remove(post1)
    post2 = random.choice(posts)
    posts.remove(post2)
    post3 = random.choice(posts)
    posts.remove(post3)

    contexto = {
        'postShow': postShow,
        'sociales': obtenerRedes,
        'web': obtenerInformacion,
        'post1': consulta(post1),
        'post2': consulta(post2),
        'post3': consulta(post3),
    }
    return render(request, 'Publicacion/postShow.html', contexto)


def suscribirse(request, *args, **kwargs):
    correo = request.POST.get('correo')
    Suscripcion.objects.create(correo=correo)
    asunto = 'Gracias Por Suscribirte A Nice Gaming'
    messages = 'Te Has Suscrito Satisfactoriamente Gracias Nos Ayudas Mucho'

    try:
        send_mail(asunto, messages, EMAIL_HOST_USER, [correo])
    except:
        pass
    return redirect('/')
