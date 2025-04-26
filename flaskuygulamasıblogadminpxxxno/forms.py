from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField,FileField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('İçerik', validators=[DataRequired()])

class UserForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(), Length(max=50)])
    email = StringField('E-posta', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Şifre', validators=[DataRequired(), Length(min=6)])
    profile_picture = FileField('Profil Resmi')  # Dosya yükleme alanı