from django.urls import path
from . import views

urlpatterns = [
    path('consulta/<int:consulta_id>/', 
         views.criar_prontuario, 
         name='prontuario_abrir'
         ),
]
