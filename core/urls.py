from django.urls import path
from .views import index,contacto,galeria,listado_cliente,nuevo_cliente,modificar_cliente,eliminar_cliente,listado_ot,modificar_ot,nuevo_ot,eliminar_ot,nuevo_tecnico,modificar_tecnico,listado_tecnico,eliminar_tecnico,registro_usuario

urlpatterns = [
    path('', index, name="index"),
    path('contacto/',contacto ,name="contacto"),
    path('galeria/',galeria ,name="galeria"),
    path('listado-clientes/', listado_cliente , name="listado_clientes"),
    path('nuevo-cliente/',nuevo_cliente, name="nuevo_cliente"),
    path('modificar-cliente/<id>/',modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/',eliminar_cliente, name="eliminar_cliente"),
    path('listado-ot/', listado_ot , name="listado_ot"),
    path('modificar-ot/<id>/',modificar_ot, name="modificar_ot"),
    path('nuevo-ot/',nuevo_ot, name="nuevo_ot"),
    path('eliminar-ot/<id>/',eliminar_ot, name="eliminar_ot"),


    path('listado-tecnico/', listado_tecnico , name="listado_tecnico"),
    path('modificar-tecnico/<id>/',modificar_tecnico, name="modificar_tecnico"),
    path('nuevo-tecnico/',nuevo_tecnico, name="nuevo_tecnico"),
    path('eliminar-tecnico/<id>/',eliminar_tecnico, name="eliminar_tecnico"),

    path('registro/',registro_usuario, name="registro_usuario")
]
