from app.forms.forms import AstralForm
from app.models.houses_model import AstroHouse
from app.models.nakshatra_model import Nakshatra
from app.models.planet_phala_model import PlanetPhala
from flask import render_template, request, send_file

# from app.extensions.pdf_utils import gerar_pdf_em_memoria


def index():
    form = AstralForm()
    context = {
        "nakshatra": None,
        "house": None,
        "planets": [],
        "house_strength": None,
        "planet_strength": None,
        "ishtaphala": None,
        "kashtaphala": None
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
            astro_house = AstroHouse(house, house_strength)


            context = {
                "nakshatra": nakshatras._lord,
                "house": astro_house._show_house(),
                "planets": planetphala._planet,
                "house_strength": astro_house._strenghts,
                "planet_strength": planetphala._strenghts,
                "ishtaphala": planetphala._ishtaphala,
                "kashtaphala": planetphala._kashtaphala,
                "verifica_casa": astro_house.check_house(),
                
            }
        except ValueError as e:
            print("Erro:", e)
    return render_template("pages/index.html", form=form, title="Astral Map", **context)




def download_pdf():
    nakshatra_name = request.args.get("nakshatra")
    if not nakshatra_name:
        return "Não encontrado", 400
    
    nakshatra = Nakshatra(nakshatra_name)

    # texts = [
    #     nakshatra._read_nakshatra_base_text_pdf(),
    #     nakshatra._select_nakshatra_text_pdf()
    # ]
    # titulos = ["Nakshatra Lunar", nakshatra._lord]

    # pdf_buffer = gerar_pdf_em_memoria(titulos, texts)

    return send_file(
       
        nakshatra.create_nakshatras_complete_text(),
        as_attachment=True,
        download_name="nakshatra_completo.pdf",
        mimetype="application/pdf"
    )