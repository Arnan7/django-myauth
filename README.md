<img width="1600" height="776" alt="image" src="https://github.com/user-attachments/assets/b72b8e79-6612-4649-b32f-c2dd2745b9be" />
<img width="1596" height="777" alt="image" src="https://github.com/user-attachments/assets/203c93dc-1854-4d9f-85b2-f6216834721d" />

# Django Auth App con Tailwind CSS

Aplicación web full-stack construida sobre Django que implementa un sistema de autenticación robusto y seguro. Utiliza un backend de autenticación personalizado ([`myauthapp.backends.EmailBackend`](src/myauthapp/backends.py)) que permite el login mediante email o nombre de usuario. El frontend está renderizado a través de plantillas de Django y estilizado con Tailwind CSS, compilado mediante un pipeline de Node.js gestionado por `django-tailwind` para un diseño moderno y responsivo. La configuración del proyecto es flexible, gestionando variables de entorno (`.env`) para claves sensibles.

## Funcionalidades Principales

-   **Autenticación Dual**: Implementación de un backend de autenticación personalizado ([`myauthapp.backends.EmailBackend`](src/myauthapp/backends.py)) que permite a los usuarios iniciar sesión con su correo electrónico o nombre de usuario, ofreciendo mayor flexibilidad.
-   **Gestión de Cuentas de Usuario**: Flujo completo de registro ([`register`](src/myauthapp/views.py)), inicio de sesión y cierre de sesión, utilizando los formularios (`UserRegisterForm`) y vistas de Django, personalizadas para la aplicación.
-   **Vistas Protegidas**: Uso del decorador `@login_required` de Django para proteger rutas críticas como el Dashboard ([`dashboard`](src/myauthapp/views.py)), asegurando que solo los usuarios autenticados puedan acceder.
-   **Interfaz Responsiva con Tailwind CSS**: Diseño de interfaz de usuario moderno construido con Tailwind CSS. Los estilos se gestionan y compilan a través de `django-tailwind`, asegurando un rendimiento óptimo.
-   **Sistema de Notificaciones**: Integración del `messages framework` de Django para proporcionar feedback visual al usuario tras acciones importantes, renderizado en la plantilla base ([`base.html`](src/templates/base.html)).
-   **Configuración Basada en Entorno**: Uso de `python-dotenv` para cargar configuraciones sensibles (ej. `SECRET_KEY`) desde un archivo `.env`, siguiendo las mejores prácticas de seguridad.

## Arquitectura y Construcción

1.  **Estructura del Proyecto**: Se organizó el código en aplicaciones Django modulares: `myauthapp` para la lógica de autenticación, `mytheme` para la gestión del tema de Tailwind, y `project_auth_app` para la configuración principal.
2.  **Backend de Autenticación**: Se desarrolló un `EmailBackend` personalizado en [`myauthapp/backends.py`](src/myauthapp/backends.py) para permitir el inicio de sesión con email.
3.  **Vistas y URLs**: Se crearon las vistas para `home`, `dashboard` y `register` en [`myauthapp/views.py`](src/myauthapp/views.py) y se mapearon a sus respectivas URLs.
4.  **Formularios Personalizados**: Se creó un `UserRegisterForm` en [`myauthapp/forms.py`](src/myauthapp/forms.py) para gestionar la creación de nuevos usuarios.
5.  **Diseño de Plantillas**: Se diseñó una plantilla base ([`base.html`](src/templates/base.html)) y plantillas específicas para cada vista (`home.html`, `dashboard.html`, `login.html`, etc.) utilizando Tailwind CSS.
6.  **Integración de Tailwind CSS**: Se configuró `django-tailwind` para integrar un pipeline de compilación de frontend. Los archivos fuente de CSS se encuentran en `src/mytheme/static_src`.
7.  **Interactividad Frontend**: Se añadió interactividad con JavaScript ([`src/static/js/script.js`](src/static/js/script.js)) y Alpine.js para elementos como el menú de navegación móvil.

## Requisitos Previos

-   Python 3.8 o superior
-   Node.js y npm
-   Git

## Instalación y Configuración desde Cero

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd djangoauth
```

### 2. Configurar el Entorno Virtual de Python

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar Dependencias de Python

Instala todas las librerías de Python necesarias desde el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

El proyecto utiliza un archivo `.env` para gestionar las claves secretas y otras configuraciones.

Crea un archivo llamado `.env` dentro de la carpeta `src/` y añade el siguiente contenido.

```ini
// filepath: src/.env
# Genera tu propia SECRET_KEY. Puedes usar un generador online.
SECRET_KEY='tu-django-secret-key-aqui'

# Ruta al ejecutable de npm en tu sistema.
# Ejemplo para Windows:
NPM_BIN_PATH='C:/Users/tu_usuario/AppData/Roaming/npm/npm.cmd'
# Ejemplo para macOS/Linux (generalmente 'npm' es suficiente si está en el PATH):
# NPM_BIN_PATH='npm'
```

### 5. Instalar Dependencias de Frontend y Compilar CSS

Usa los comandos de `django-tailwind` para instalar las dependencias de Node.js y compilar los estilos de Tailwind CSS. Estos comandos deben ejecutarse desde el directorio `src/`.

```bash
# Instala las dependencias de npm (ejecutar desde src/)
python manage.py tailwind install

# Compila los estilos de Tailwind para producción
python manage.py tailwind build
```

### 6. Preparar la Base de Datos

Ejecuta las migraciones de Django para crear las tablas necesarias en la base de datos `db.sqlite3`.

```bash
# Asegúrate de estar en el directorio 'src/'
cd src

# Aplica las migraciones
python manage.py migrate
```

### 7. Crear un Superusuario

Crea una cuenta de administrador para poder acceder al panel de administración de Django.

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el Servidor de Desarrollo

¡Todo está listo! Inicia el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

El sitio estará disponible en `http://127.0.0.1:8000`.

## Comandos Útiles

-   **Iniciar el servidor de Django**:
    ```bash
    # Desde la carpeta src/
    python manage.py runserver
    ```

-   **Compilar Tailwind CSS en modo desarrollo (con auto-recarga)**:
    ```bash
    # Desde la carpeta src/
    python manage.py tailwind start
    ```

-   **Compilar Tailwind CSS para producción**:
    ```bash
    # Desde la carpeta src/
    python manage.py tailwind build
    ```
