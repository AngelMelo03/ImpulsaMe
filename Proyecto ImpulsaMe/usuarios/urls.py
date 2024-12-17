from django.urls import path
from .views import inicio, docente_view, area_ciencia, area_estudiantes, principal, registro, registro_docente, registro_estudiante, estudiante_principal, profesores_por_area
from django.contrib.auth import views as auth_views
from . import views
from django.http import HttpResponse



urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('ciencia/', area_ciencia, name='area_ciencia'),
    path('inicio/', inicio, name='inicio'),
    path('ciencia/', area_ciencia, name='area_ciencia'),
    path('estudiantes/', area_estudiantes, name='area_estudiantes'),
    path('', principal, name='principal'),
    path('registro/', registro, name='registro'),  # Vista principal de registro
    path('registro/docente/', registro_docente, name='registro_docente'),  # Registro de docente
    path('registro/estudiante/', registro_estudiante, name='registro_estudiante'),  # Registro de estudiante
    path('estudiante/', estudiante_principal, name='estudiante_principal'),
    path('area/<str:area>/', profesores_por_area, name='profesores_por_area'),
    path('login/', views.principal, name='login'),  # Agregar esta línea

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('docente/', views.docente_view, name='docente_principal'),  # Nombre correcto aquí
    path('send_message/<int:recipient_id>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    

    path('modificar_cuenta/', views.modificar_cuenta, name='modificar_cuenta'),
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),

]