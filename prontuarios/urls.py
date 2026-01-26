from django.urls import path
from . import views

urlpatterns = [
    path("", views.prontuarios_home, name="prontuarios_home"),
    path('consulta/<int:consulta_id>/', views.criar_prontuario, name='prontuario_abrir'),
]
