from flask import Flask, jsonify
from app.db import db, ma
from conf.config import DevelopmentConfig
from app.products.views import products
from app.auth.views import auth
from app.payment.views import payment
from app.shopping.views import car
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_login import LoginManager, logout_user
from app.auth.models import User

ACTIVE_ENDPOINTS = [('/products', products),('', auth),('/payment', payment),('/car', car)]
SAWGGER_URL = '/swagger'
API_URL = '/spec'
swagger_blueprint = get_swaggerui_blueprint(SAWGGER_URL, API_URL, config={'app-name': "pygroup-web"})

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    app.config.from_object(config)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        db.create_all()

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/spec')
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0.0"
        swag['info']['title'] = "pygroup-Web"
        swag['info']['description'] = "My shop example using Flask"
        return jsonify(swag)

    app.register_blueprint(swagger_blueprint, url_prefix = SAWGGER_URL)

    return app


if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()
