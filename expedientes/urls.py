from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('persona/<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
    path('persona/nueva/', views.nueva_persona, name='nueva_persona'),
    path('persona/<int:persona_id>/editar/', views.editar_persona, name='editar_persona'),
]

