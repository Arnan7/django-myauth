# --- myauthapp/backends.py ---
# Este archivo define cómo Django autenticará a los usuarios.
# Aquí, permitimos iniciar sesión usando el correo electrónico.

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    """
    Backend de autenticación mejorado que permite iniciar sesión con el correo electrónico
    de forma insensible a mayúsculas y minúsculas.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # El campo 'username' del formulario de login contendrá el email del usuario.
        # Buscamos un usuario por su email, ignorando mayúsculas/minúsculas.
        # .first() es más seguro que .get() porque evita excepciones si no hay resultados o hay múltiples.
        user = User.objects.filter(email__iexact=username).first()

        # Si se encontró un usuario, verificamos su contraseña y si su cuenta está activa.
        # `self.user_can_authenticate(user)` comprueba flags como `is_active`.
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        # Si no se encuentra un usuario o la contraseña es incorrecta, devolvemos None.
        # Django intentará automáticamente el siguiente backend en la lista (ModelBackend).
        return None

    # No es necesario redefinir get_user, ya que ModelBackend ya lo implementa correctamente.
    # Al heredar de ModelBackend, esta funcionalidad ya está incluida.
