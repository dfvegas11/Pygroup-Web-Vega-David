from flask import Blueprint, Response

prod = Blueprint('prod',__name__,url_prefix='/prod')

@prod.route('/<name>', methods=['GET'])
def index(name):
    if name!="pygroup":
        return Response ("Felicitaciones! Trabajo exitoso {}".format(name), status=200)
    return Response ("ERROR! No se puede usar el nombre pygroup", status=400)


"""Flask te permite usar plantillas para el contenido dinámico de páginas web.
Una de las cosas más sencillas que se pueden hacer en Flask es crear una página web ante una petición. 
Es decir, usar un template en Flask que sea una página HTML a la cual 
podemos insertar contenido recuperado desde nuestro programa Python.
A este método debemos pasarle el nombre de nuestra plantilla y las variables
necesarias para su renderizado como parámetros clave-valor."""