from .models import Categoria, Informacion, Post, RedesSociales

def consulta(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def obtenerRedes():
    return RedesSociales.objects.filter(
        estado = True
    ).latest('fecha_creacion')

def obtenerInformacion():
    return Informacion.objects.filter(
        estado = True
    ).latest('fecha_creacion')