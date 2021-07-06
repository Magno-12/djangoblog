from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','state','fecha_creacion')
    resources_class = CategoriaResource

class AuthorResource(resources.ModelResource):
    model = Author


class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['names','second_name']
    list_display = ('names','second_name','estado','fecha_de_creacion',)
    resources_class = AuthorResource


class PostResource(resources.ModelResource):
    model = Post


class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','slug','descripcion']
    list_display = ('titulo','slug','descripcion','fecha_creacion',)
    resources_class = PostResource


admin.site.register(Category, CategoriaAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post,PostAdmin)
