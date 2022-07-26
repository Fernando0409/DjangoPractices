from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.incio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name="libros"),
    path('libros/crear', views.crearLibro, name="crearLibro"),
    path('libros/editar', views.editar, name='editarLibro'),
    path('eliminar/<int:id>', views.eliminar, name='eliminarLibro'),
    path('libros/editar/<int:id>', views.editar, name='editarLibro'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)