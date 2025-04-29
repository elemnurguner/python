from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename

class FilmEkleForm(FlaskForm):
    ad = StringField("Film Adı", validators=[DataRequired(), Length(min=2, max=100)])
    resim = FileField("Film Afişi", validators=[DataRequired()])
    submit = SubmitField("Filmi Ekle")
