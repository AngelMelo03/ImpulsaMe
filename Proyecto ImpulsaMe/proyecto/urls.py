from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Vistas temporales para probar redirecciones
def inicio(request):
    return HttpResponse('<h1>Página de inicio</h1>')

def area_ciencia(request):
    return HttpResponse('<h1>Área de Ciencia</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', include('usuarios.urls')),
    path('inicio/', inicio, name='inicio'),
    path('ciencia/', area_ciencia, name='area_ciencia'),
]
