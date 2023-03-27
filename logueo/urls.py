from django.urls import path
from logueo import views
from colegio.views import home

urlpatterns = [
    path('', views.home,name='iniciar_sesion'),
    path('iniciaste_sesion/',views.loginsesiondef, name='iniciaste_sesion'),
    path('creaste_usuario/',views.regissesiondef, name='registro_sesion'),
    path('gestionproducto/',home, name='gestion_producto'),
]