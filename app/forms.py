from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    uName = StringField("Username", validators=[InputRequired(), Length(min=2, max=50)])
    uDob = DateField("Date of Birth", format='%Y-%m-%d', validators=[InputRequired()])
    uPass = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    uGender = SelectField("Gender", choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[InputRequired()])
    submit = SubmitField("Register")
