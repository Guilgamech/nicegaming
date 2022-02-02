from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la categoria)', max_length=100, unique=True)
    imagen_refer = models.ImageField('Imagen de referencia ', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Autor(ModeloBase):
    nombre = models.CharField('Nombre de autor', max_length=100)
    correo = models.EmailField('Correo electronico', max_length=254)
    descripcion = models.TextField('Descripcion')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre


class Post(ModeloBase):
    titulo = models.CharField('Titulo de la publicacion', max_length=150, unique=True)
    slug = models.CharField('Asunto', max_length=50)
    descripcion = models.TextField('descripcion de el post')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_refer = models.ImageField('Imagen referencial', upload_to='imagenes/', height_field=None, width_field=None,
                                     max_length=255)
    publicado = models.BooleanField('Publicado /No publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de publicacion')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo


class Informacion(ModeloBase):
    us = models.TextField('Nosotros')
    telefono = models.CharField('Telefono compañia', max_length=50)
    email = models.EmailField('Correo compañia', max_length=254)
    direccion = models.CharField('Direccion compañia', max_length=200)

    class Meta:
        verbose_name = 'Informacon'
        verbose_name_plural = 'Informaciones'

    def __str__(self):
        return self.us


class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook', max_length=200)
    Twitter = models.URLField('Twitter', max_length=200)
    Linkendin = models.URLField('Linkendin', max_length=200)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook


class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Correo usuario', max_length=254)
    asunto = models.CharField('Asunto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto


class Suscripcion(ModeloBase):
    correo = models.EmailField('Correo subcritor', max_length=254)

    class Meta:
        verbose_name = 'Supcricion'
        verbose_name_plural = 'Supcripciones'

    def __str__(self):
        return self.correo
