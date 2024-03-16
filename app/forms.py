from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Formulario de preenchimento da latitude e longitude para buscar valores atraves da Api
class FormularioClima(FlaskForm):
  latitude = StringField('Latitude', validators=[DataRequired()], render_kw={'placeholder':'Latitude'})
  longitude = StringField('Longitude', validators=[DataRequired()], render_kw={'placeholder':'Longitude'})
  btn_pesquisar = SubmitField('Pesquisar')