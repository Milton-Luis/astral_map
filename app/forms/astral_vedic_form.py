from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, ValidationError, widgets
from wtforms.fields import SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired


class SingleAstralForm(FlaskForm):
    class Meta:
        csrf = False

    house = StringField("Casa", validators=[DataRequired()])
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
    houses = FieldList(FormField(SingleAstralForm), min_entries=2, max_entries=12)
    submit = SubmitField("Enviar")
