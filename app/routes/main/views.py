from astral_map.app.forms.astral_vedic_form import AstralForm
from app.models.houses_model import AstroHouse
from app.models.nakshatra_model import Nakshatra
from app.models.planet_phala_model import PlanetPhala
from flask import flash, render_template, request, send_file
from dynaconf import settings

from astral_map.app.forms.config_forms import BaseValueHouse, BaseValueplanet


def index():
    form = AstralForm()
    context = {
        "nakshatra": None,
        "house": None,
        "planets": [],
        "house_strength": None,
        "planet_strength": None,
        "ishtaphala": None,
        "kashtaphala": None,
    }

    if form.validate_on_submit():
        nakshatra = form.nakshatra.data
        house = form.house.data
        planets = form.planet.data
        house_strength = form.house_strengths.data
        planet_strength = form.planet_strengths.data
        ishtaphala = form.ishtaphala.data
        kashtaphala = form.kashtaphala.data
        try:
            nakshatras = Nakshatra(nakshatra)
            planetphala = PlanetPhala(planets, ishtaphala, kashtaphala, planet_strength)
            astro_house = AstroHouse(house, house_strength, planets)

            context = {
                "nakshatra": nakshatras._lord,
                "house": astro_house._show_house(),
                "planets": planetphala._planet,
                "house_strength": astro_house._strengths,
                "planet_strength": planetphala._strengths,
                "ishtaphala": planetphala._ishtaphala,
                "kashtaphala": planetphala._kashtaphala,
            }
        except ValueError as e:
            print("Erro:", e)
    return render_template("pages/index.html", form=form, title=settings.PDF_TITLE, **context)


def download_pdf():
    nakshatra_name = request.args.get("nakshatra")
    if not nakshatra_name:
        return "Não encontrado", 400

    nakshatra = Nakshatra(nakshatra_name)

    try:
        return send_file(
            nakshatra.create_nakshatras_complete_text(),
            as_attachment=True,
            download_name="nakshatra_completo.pdf",
            mimetype="application/pdf",
        )
    except Exception as e:
        flash("Erro ao criar documento", "danger")
        raise e
        # return redirect(url_for("main.index"))

def settings():
    house_form = BaseValueHouse()
    planet_form = BaseValueplanet()