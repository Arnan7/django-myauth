# --- myauthapp/forms.py ---
# Este archivo define los formularios para tu aplicación.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    # Campo de correo electrónico, visible y requerido en el registro.
    email = forms.EmailField(label='Correo electrónico', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        # Definimos el orden de los campos en el formulario de registro.
        # 'username' y 'email' se mostrarán primero, luego las contraseñas.
        fields = ('username', 'email') + UserCreationForm.Meta.fields[1:]

    def clean_email(self):
        email = self.cleaned_data['email']
        # Validación: Asegura que el correo electrónico no esté ya en uso.
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def save(self, commit=True):
        # Guarda el usuario. El username y email se toman directamente del formulario.
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'] # Asegura que el email se guarda correctamente
        if commit:
            user.save()
        return user
