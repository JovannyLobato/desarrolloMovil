from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('persona/<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
]

