from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('generales/',generales, name = 'generales'),
    path('iot/',iot, name = 'iot'),
    path('tech/',tech, name = 'tech'),
    path('nigeria/',nigeria, name = 'nigeria'),
    path('<slug:slug>/',detallePost, name='detalle_post'),



]