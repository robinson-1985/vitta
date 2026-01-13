from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta_list, name='consulta_list'),
    path('nova/', views.consulta_create, name='consulta_create'),
    path('<int:pk>/editar/', views.consulta_update, name='consulta_update'),
    path('<int:pk>/excluir/', views.consulta_delete, name='consulta_delete'),
]
