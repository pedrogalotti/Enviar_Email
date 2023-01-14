from django.urls import path

from . import views

urlpatterns = [
    path('enviar/', views.enviar_email, name="enviar-email"),
]