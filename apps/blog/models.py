from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la categoria',
                            max_length=100, null=False, blank=False)
    state = models.BooleanField(
        'Categoría Activada/Categoría no Activada', default=True)
    fecha_creacion = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(
        'Nombres del Autor', max_length=255, null=False, blank=False)
    second_name = models.CharField(
        'Apellidos del Autor', max_length=255, null=False, blank=False)
    Facebook = models.URLField('Facebook', null=True, blank=True)
    Twitter = models.URLField('Twitter', null=True, blank=True)
    Instagram = models.URLField('Instagram', null=True, blank=True)
    Youtube = models.URLField('Youtube', null=True, blank=True)
    Web_site = models.URLField('Web Site', null=True, blank=True)
    Email = models.EmailField('Email', blank=True, null=True)
    estado = models.BooleanField(
        'Active Author/Not Active Author', default=True)
    fecha_de_creacion = models.DateField(
        'Creation date', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return "{0},{1}".format(self.second_name, self.names)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField(
        'Descripcion', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
