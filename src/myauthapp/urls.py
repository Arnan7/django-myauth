from django.urls import path
from . import views # Importa las vistas de tu aplicación

urlpatterns = [
    path('', views.home, name='home'), # URL para la página de inicio
    path('dashboard/', views.dashboard, name='dashboard'), # URL para el panel de control
    path('register/', views.register, name='register'), # URL para el registro de usuarios
]