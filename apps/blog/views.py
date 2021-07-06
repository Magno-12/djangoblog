from django.core import paginator
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils import tree
from .models import Category, Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    QuerySet = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)
    if QuerySet:
        posts = Post.objects.filter(
            Q(titulo__icontains=QuerySet) |
            Q(descripcion__icontains=QuerySet)
        ).distinct()

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post)
    return render(request, 'post.html', {'detalle_post': post})


def generales(request):
    QuerySet = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True, Category=Category.objects.get(name__iexact='Generales'))
    if QuerySet:
            posts = Post.objects.filter(
                Q(titulo__icontains=QuerySet) |
                Q(descripcion__icontains=QuerySet),
                estado = True,
                Category = Category.objects.get(name__iexact='Generales'),
                ).distinct()
    return render(request, 'generales.html', {'posts': posts})


def iot(request):
    QuerySet = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True, Category=Category.objects.get(name__iexact='IOT'))
    if QuerySet:
            posts = Post.objects.filter(
                Q(titulo__icontains=QuerySet) |
                Q(descripcion__icontains=QuerySet),
                estado = True,
                Category = Category.objects.get(name__iexact='IOT'),
                ).distinct()
    return render(request, 'iot.html', {'posts': posts})


def tech(request):
    QuerySet = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True, Category=Category.objects.get(name__iexact='Tecnologia'))
    if QuerySet:
            posts = Post.objects.filter(
                Q(titulo__icontains=QuerySet) |
                Q(descripcion__icontains=QuerySet),
                estado = True,
                Category = Category.objects.get(name__iexact='Tecnologia'),
                ).distinct()
    return render(request, 'tech.html', {'posts': posts})


def nigeria(request):
    QuerySet = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado=True, Category=Category.objects.get(name__iexact='Nigeria'))
    if QuerySet:
            posts = Post.objects.filter(
                Q(titulo__icontains=QuerySet) |
                Q(descripcion__icontains=QuerySet),
                estado = True,
                Category = Category.objects.get(name__iexact='Nigeria'),
                ).distinct()
    return render(request, 'nigeria.html', {'posts': posts})
