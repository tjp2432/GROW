from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, BooleanField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])

class ProductForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    short_description = StringField('Descripción Corta', validators=[Length(max=300)])
    price = FloatField('Precio', validators=[DataRequired(), NumberRange(min=0)])
    compare_price = FloatField('Precio Comparativa', validators=[Optional()])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)], default=0)
    category_id = SelectField('Categoría', coerce=int, validators=[DataRequired()])
    featured = BooleanField('Destacado')
    active = BooleanField('Activo', default=True)

class BlogForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=200)])
    excerpt = StringField('Extracto', validators=[Length(max=400)])
    content = TextAreaField('Contenido', validators=[DataRequired()])
    author = StringField('Autor', validators=[Length(max=100)])
    category = StringField('Categoría', validators=[Length(max=100)])
    tags = StringField('Tags', validators=[Length(max=300)])
    published = BooleanField('Publicado')
    featured = BooleanField('Destacado')

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Asunto', validators=[Length(max=200)])
    message = TextAreaField('Mensaje', validators=[DataRequired()])

class CheckoutForm(FlaskForm):
    full_name = StringField('Nombre Completo', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Teléfono', validators=[Length(max=20)])
    address = StringField('Dirección', validators=[DataRequired(), Length(max=300)])
    city = StringField('Ciudad', validators=[DataRequired(), Length(max=100)])
    state = StringField('Provincia', validators=[Length(max=100)])
    zip_code = StringField('Código Postal', validators=[Length(max=20)])
    notes = TextAreaField('Notas', validators=[Length(max=500)])
