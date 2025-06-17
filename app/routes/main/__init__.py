from flask import Blueprint

from . import views

main = Blueprint("main", __name__)


main.add_url_rule("/", view_func=views.index, endpoint="index", methods=["POST", "GET"])

main.add_url_rule(
    "/",
    view_func=views.settings_astral_vedic_values,
    endpoint="settings_astral_vedic_values",
    methods=["POST", "GET"],
)
main.add_url_rule("/dowload", view_func=views.download_pdf, endpoint="download")
