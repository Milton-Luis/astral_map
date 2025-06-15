import os

from dynaconf import FlaskDynaconf


def init_app(app):
    FlaskDynaconf(app)


# def init_app():
#     settings = Dynaconf(
#         settings_files=["settings.toml", ".env"], environments=True, load_dotenv=True
#     )
#     return settings

# settings = init_app()
