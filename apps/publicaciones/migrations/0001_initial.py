# Generated by Django 4.0.1 on 2022-02-02 17:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de autor')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoria)')),
                ('imagen_refer', models.ImageField(upload_to='categoria/', verbose_name='Imagen de referencia ')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo usuario')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('us', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono compañia')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo compañia')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion compañia')),
            ],
            options={
                'verbose_name': 'Informacon',
                'verbose_name_plural': 'Informaciones',
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('Twitter', models.URLField(verbose_name='Twitter')),
                ('Linkendin', models.URLField(verbose_name='Linkendin')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo subcritor')),
            ],
            options={
                'verbose_name': 'Supcricion',
                'verbose_name_plural': 'Supcripciones',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo de la publicacion')),
                ('slug', models.CharField(max_length=50, verbose_name='Asunto')),
                ('descripcion', models.TextField(verbose_name='descripcion de el post')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_refer', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen referencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado /No publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.categoria')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.autor')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
