# --- myauthapp/views.py ---
# Este archivo contiene la lógica de las páginas de tu aplicación.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Decorador para proteger vistas
from .forms import UserRegisterForm
from django.contrib import messages # Para mostrar mensajes al usuario

# Vista para la página de inicio (accesible para todos).
def home(request):
    return render(request, 'home.html')

# Vista para el panel de control (solo accesible para usuarios autenticados).
@login_required # Si el usuario no está logueado, será redirigido a la página de login.
def dashboard(request):
    # Pasa información sobre si el usuario es superusuario y si tiene permiso para acceder al admin panel.
    is_superuser = request.user.is_superuser
    can_access_admin = request.user.has_perm('admin.view_logentry')  # Reemplaza 'admin.view_logentry' con el permiso correcto si es necesario.
    return render(request, 'dashboard.html', {'is_superuser': is_superuser, 'can_access_admin': can_access_admin})

# Vista para el registro de nuevos usuarios.
def register(request):
    if request.method == 'POST':
        # Si el formulario fue enviado (POST), procesa los datos.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos son válidos, crea el nuevo usuario.
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'¡Cuenta creada para {email}! Ahora puedes iniciar sesión con tu correo electrónico.')
            return redirect('login') # Redirige al login.
    else:
        # Si es una solicitud GET, muestra un formulario vacío.
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})