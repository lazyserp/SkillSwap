from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, Length,DataRequired

class RegisterForm(FlaskForm):
    uName = StringField("Username", validators=[InputRequired(), Length(min=2, max=50)])
    uDob = DateField("Date of Birth", format='%Y-%m-%d', validators=[InputRequired()])
    uPass = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    uGender = SelectField("Gender", choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[InputRequired()])
    submit = SubmitField("Register")
    skills_offered = StringField('Skills You can teach')
    skills_needed = StringField('Skills you want to learn')
    bio = TextAreaField('Your Bio')



class LoginForm(FlaskForm):
    uName = StringField('Username', validators=[DataRequired()])
    uPass= PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ForgotPasswdForm(FlaskForm):
    uName = StringField('Username: ',validators=[InputRequired()])
    new_pass = PasswordField('New Password: ',validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm New Password: ',validators=[InputRequired()])
    submit = SubmitField('Reset Password')