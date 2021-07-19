from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, BooleanField


class CarsForm(FlaskForm):
    id = StringField('Id',  validators=[DataRequired()])
    marka = StringField('Marka', validators=[DataRequired()])
    model = StringField('Model ', validators=[DataRequired()])
    rocznik = IntegerField('Rocznik', validators=[DataRequired()])
    kolor = StringField('Kolor', validators=[DataRequired()])
    moc = IntegerField('Moc', validators=[DataRequired()])
    czy_bezwypadkowy = BooleanField('Czy bezwypadkowy?',validators=[DataRequired()])