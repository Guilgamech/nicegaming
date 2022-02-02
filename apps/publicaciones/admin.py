from django.contrib import admin

# Register your models here.
from apps.publicaciones.models import *

admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Informacion)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
admin.site.register(Suscripcion)