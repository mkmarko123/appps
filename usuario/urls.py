from django.urls import path
from usuario import views


app_name = 'usuario'


urlpatterns = [
    path('registro/', views.crear_usuario, name='registro'),
    path('inicio/', views.inicio_sesion, name='inicio'),
]