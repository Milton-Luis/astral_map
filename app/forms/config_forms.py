from flask_wtf import FlaskForm
from wtforms import ValidationError, widgets
from wtforms.fields import IntegerField, SubmitField
from wtforms.validators import DataRequired


class BaseValueHouse(FlaskForm):
    house_high_value = IntegerField(
        "Valor alto da casa", validators=[DataRequired()], default=50
    )
    house_mid_value = IntegerField(
        "Valor moderado da casa", validators=[DataRequired()], default=30
    )
    house_low_value = IntegerField(
        "Valor baixo da casa", validators=[DataRequired()], default=10
    )

    submit = SubmitField("Atualizar casa")


class BaseValueplanet(FlaskForm):
    house_high_value = IntegerField(
        "Valor alto do planeta em %", validators=[DataRequired()], default=200
    )
    house_mid_value = IntegerField(
        "Valor moderado do planeta em %", validators=[DataRequired()], default=100
    )
    house_low_value = IntegerField(
        "Valor baixo do planeta em %", validators=[DataRequired()], default=50
    )

    submit = SubmitField("Atualizar planeta")
