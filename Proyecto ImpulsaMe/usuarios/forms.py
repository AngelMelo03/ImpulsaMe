from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class EstudianteRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        

class DocenteRegistroForm(UserCreationForm):
    area_ensenanza = forms.ChoiceField(
        choices=[
            ('ciencia', 'Ciencia'),
            ('cultura', 'Cultura'),
            ('salud', 'Salud'),
        ],
        required=True,
        label="Área de enseñanza"
    )
    cargo = forms.CharField(max_length=100, required=True, label="Cargo")
    experiencia = forms.CharField(widget=forms.Textarea, required=True, label="Experiencia")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'area_ensenanza', 'cargo', 'experiencia']


# forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'cargo', 'experiencia']
