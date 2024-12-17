from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import EstudianteRegistroForm, DocenteRegistroForm, UsuarioUpdateForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Message
from .forms import MessageForm

def registro(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')
        if tipo_usuario == 'docente':
            return redirect('registro_docente')
        elif tipo_usuario == 'estudiante':
            return redirect('registro_estudiante')
    return render(request, 'usuarios/registro_opcion.html')

def registro_docente(request):
    form = DocenteRegistroForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.tipo_usuario = 'docente'
        usuario.save()
        return redirect('principal')  # Redirige al login después de registrarse
    return render(request, 'usuarios/registro_docente.html', {'form': form})

def registro_estudiante(request):
    form = EstudianteRegistroForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.tipo_usuario = 'estudiante'
        usuario.save()
        return redirect('principal')  # Redirige al login después de registrarse
    return render(request, 'usuarios/registro_estudiante.html', {'form': form})


# Vista para la página de inicio
@login_required
def inicio(request):
    return render(request, 'usuarios/inicio.html')

# Vista para el área de docentes
@login_required
def area_ciencia(request):
    return render(request, 'usuarios/area_ciencia.html')

# Vista para el área de estudiantes (si se requiere)
@login_required
def area_estudiantes(request):
    return render(request, 'usuarios/area_estudiantes.html')

def principal(request):  # Vista para login
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.tipo_usuario == 'docente':
                return redirect('docente_principal')  # Página principal para docentes
            elif user.tipo_usuario == 'estudiante':
                return redirect('estudiante_principal')  # Página principal para estudiantes
        else:
            error = "Usuario o contraseña incorrectos."
    return render(request, 'usuarios/principal.html', {'error': error})

@login_required
def estudiante_principal(request):  # Vista para estudiantes
    if request.user.tipo_usuario != 'estudiante':
        return redirect('docente_principal')  # Evita que otros roles accedan
    return render(request, 'usuarios/estudiante_principal.html')

@login_required
def docente_principal(request):  # Vista para docentes
    if request.user.tipo_usuario != 'docente':
        return redirect('estudiante_principal')  # Evita que otros roles accedan
    return render(request, 'usuarios/docente_principal.html')


def profesores_por_area(request, area):
    # Filtrar los profesores por área de enseñanza
    profesores = Usuario.objects.filter(tipo_usuario='docente', area_ensenanza=area)
    return render(request, 'usuarios/profesores_area.html', {'profesores': profesores, 'area': area})


@login_required
def docente_view(request):
    if request.user.tipo_usuario != 'docente':
        return redirect('estudiante')  # Redirige a la página de estudiantes si no es docente
    return render(request, 'usuarios/docente.html')


def logout_view(request):
    logout(request)
    return redirect('principal')
    

User = get_user_model()    
@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('inbox')  # Redirige a la bandeja de entrada
    else:
        form = MessageForm()
    return render(request, 'usuarios/send_message.html', {'form': form, 'recipient': recipient})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'usuarios/inbox.html', {'messages': messages})

from django.contrib.auth.decorators import login_required

@login_required
def modificar_cuenta(request):
    usuario = request.user
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('estudiante_principal' if usuario.tipo_usuario == 'estudiante' else 'docente_principal')
    else:
        form = UsuarioUpdateForm(instance=usuario)
    return render(request, 'usuarios/modificar_cuenta.html', {'form': form})

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('principal')
    return render(request, 'usuarios/eliminar_cuenta.html')

