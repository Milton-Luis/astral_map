from app.extensions import configuration
from flask import Flask


def register_blueprint_on_app(app):
    from app.routes.main import main as main_blueprint

    app.register_blueprint(main_blueprint)


def create_app():
    app = Flask(__name__)

    configuration.init_app(app)
    # configuration.load_extensions(app)
    register_blueprint_on_app(app)

    @app.template_filter("type")
    def jinja_type(value):
        return type(value).__name__

    return app


# settings = configuration.settings

# from models.nakshatra_model import Nakshatra

# nakshatra = Nakshatra("A")


# file = nakshatra.open_file("text.txt")
# print(file)
