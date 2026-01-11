from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pacientes_index'),
    path('novo/', views.criar, name='pacientes_criar'),
    path('<int:id>/editar/', views.editar, name='pacientes_editar'),
    path('<int:id>/deletar/', views.deletar, name='pacientes_deletar'),
]
