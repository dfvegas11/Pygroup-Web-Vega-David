from flask import Blueprint, Response

prod = Blueprint('prod',__name__,url_prefix='/prod')

@prod.route('/<name>', methods=['GET'])
def index(name):
    if name!="pygroup":
        return Response ("Felicitaciones! Trabajo exitoso {}".format(name), status=200)
    return Response ("ERROR! No se puede usar el nombre pygroup", status=400)