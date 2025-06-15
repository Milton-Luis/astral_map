from flask_wtf import FlaskForm
from wtforms import ValidationError, widgets
from wtforms.fields import (SelectField, SelectMultipleField, StringField,
                            SubmitField)
from wtforms.validators import DataRequired


class AstralForm(FlaskForm):
    nakshatra = SelectField(
        "Nakshatras",
        validators=[DataRequired()],
        choices=[
            ("ANURADHA", "ANURADHA"),
            ("ARDRA", "ARDRA"),
            ("ASHLESHA", "ASHLESHA"),
            ("ASHVINI", "ASHVINI"),
            ("BHARANI", "BHARANI"),
            ("CHITRA", "CHITRA"),
            ("DHANISHTA", "DHANISHTA"),
            ("HASTA", "HASTA"),
            ("JYESHTHA", "JYESHTHA"),
            ("KRITTIKA", "KRITTIKA"),
            ("MAGHA", "MAGHA"),
            ("MRIGASHIRA", "MRIGASHIRA"),
            ("MULA", "MULA"),
            ("PUNARVASU", "PUNARVASU"),
            ("PUSHYA", "PUSHYA"),
            ("PURVA ASHADHA", "PURVA ASHADHA"),
            ("PURVA BHADRAPADA", "PURVA BHADRAPADA"),
            ("PURVA PHALGUNI", "PURVA PHALGUNI"),
            ("REVATI", "REVATI"),
            ("ROHINI", "ROHINI"),
            ("SHATABHISHA", "SHATABHISHA"),
            ("SHRAVANA", "SHRAVANA"),
            ("SVATI", "SVATI"),
            ("UTTARA ASHADHA", "UTTARA ASHADHA"),
            ("UTTARA BHADRAPADA", "UTTARA BHADRAPADA"),
            ("UTTARA PHALGUNI", "UTTARA PHALGUNI"),
            ("VISHAKHA", "VISHAKHA"),
        ],
    )
    house = SelectField(
        "Casa",
        validators=[DataRequired()],
        choices=[
            (1, "1ª Casa: A Casa do Eu (Tanu Bhava)"),
            (2, "2ª Casa: Riqueza e Família (Dhana Bhava)"),
            (3, "3ª Casa: Comunicação e Coragem (Sahaja Bhava)"),
            (4, "4ª Casa: Lar e Felicidade (Sukha Bhava)"),
            (5, "5ª Casa: Criatividade e Filhos (Putra Bhava)"),
            (6, "6ª Casa: Trabalho e Saúde (Shatru Bhava)"),
            (7, "7ª Casa: Parcerias e Casamento (Kalatra Bhava)"),
            (8, "8ª Casa: Transformação e Segredos (Ayur Bhava)"),
            (9, "9ª Casa: Sabedoria e Espiritualidade (Dharma Bhava)"),
            (10, "10ª Casa: Carreira e Reputação (Karma Bhava)"),
            (11, "11ª Casa: Ganhos e Desejos (Labha Bhava)"),
            (12, "12ª Casa: Perdas e Liberação (Vyaya Bhava)"),
        ],
    )
    planet = SelectMultipleField(
        "Planeta",
        choices=[
            ("Sol", "Sol"),
            ("Lua", "Lua"),
            ("Marte", "Marte"),
            ("Mercúrio", "Mercúrio"),
            ("Jupíter", "Jupíter"),
            ("Vênus", "Vênus"),
            ("Saturno", "Saturno"),
            ("Nenhum", "Nenhum"),
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
    )
    house_strengths = StringField("Força da Casa", validators=[DataRequired()])
    planet_strengths = StringField("Força do Planeta", validators=[DataRequired()])
    ishtaphala = StringField("Ishtaphala", validators=[DataRequired()])
    kashtaphala = StringField("Kashtaphala", validators=[DataRequired()])

    submit = SubmitField("Enviar")

    def validate_planet(self, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError("Selecione pelo menos um planeta.")
