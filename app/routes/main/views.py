from app.forms.astral_vedic_form import AstralForm
from app.models.houses_model import AstroHouse
from app.models.nakshatra_model import Nakshatra
from app.models.planet_phala_model import PlanetPhala
from flask import flash, render_template, request, send_file


from app.forms.config_forms import BaseValueHouse, BaseValueplanet


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

    houses_data = []

    if form.validate_on_submit():
        nakshatra = form.nakshatra.data

        for house_form in form.houses:
            houses_data.append({
                "house": house_form.house.data,
                "planets": house_form.planet.data,
                "house_strength": house_form.house_strengths.data,
                "planet_strength": house_form.planet_strengths.data,
                "ishtaphala": house_form.ishtaphala.data,
                "kashtaphala": house_form.kashtaphala.data,
            })

        # Aqui você pode usar o primeiro item como exemplo
        if houses_data:
            try:
                nakshatras = Nakshatra(nakshatra)
                planetphala = PlanetPhala(
                    houses_data[0]["planets"],
                    houses_data[0]["ishtaphala"],
                    houses_data[0]["kashtaphala"],
                    houses_data[0]["planet_strength"],
                )
                astro_house = AstroHouse(
                    houses_data[0]["house"],
                    houses_data[0]["house_strength"],
                    houses_data[0]["planets"]
                )
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
    return render_template(
            "pages/index.html", form=form, title="astral test", **context, houses_data=houses_data
        )


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


def settings_astral_vedic_values():
    house_settings_form = BaseValueHouse()
    planet_settings_form = BaseValueplanet()
    if house_settings_form.validate_on_submit():
        ...

    if planet_settings_form.validate_on_submit():
        ...
    return render_template(
        "pages/index.html",
        title="astral test",
    )
