from flask import Flask, jsonify
from app.db import db, ma
from conf.config import DevelopmentConfig
from app.products.views import products
from app.auth.views import auth
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

ACTIVE_ENDPOINTS = [('/products', products),('', auth)]
SAWGGER_URL = '/swagger'
API_URL = '/spec'
swagger_blueprint = get_swaggerui_blueprint(SAWGGER_URL, API_URL, config={'app-name': "pygroup-web"})

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    @app.route('/spec')
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0.0"
        swag['info']['title'] = "pygroup-Web"
        swag['info']['description'] = "My shop example using Flask"
        return jsonify(swag)
    
    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_dictory()

    app.register_blueprint(swagger_blueprint, url_prefix = SAWGGER_URL)

    return app

    



if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()



""" TAREA VISTAS
app = Flask(__name__)
app.register_blueprint(name)

if __name__ == "__main__":
    app.run(debug=True)
"""
