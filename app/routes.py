from flask import Blueprint, render_template,redirect,request,url_for,session
from wtforms import Form,StringField,validators,DateTimeField,PasswordField,SelectField


class UserRegisterationForm(Form):
    uName = StringField("Name: ",validators=[validators.InputRequired(),validators.length(min=2)])
    uDob = DateTimeField("Date of Birth: ",validators=[validators.InputRequired()],format= '%Y-%m-%d')
    uPass = PasswordField("Password: ",validators=[validators.InputRequired(),validators.length(min=8,max=150)])
    uGender = SelectField("Gender: ",validators=[validators.InputRequired()],choices=[(1,"Male"),(2,"Female")])
main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('homepage.html.j2' )


@main.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        user_name = request.form['username']
    return render_template('login.html.j2')


@main.route('/register',methods=["GET","POST"])
def register_user():
    reg_form = UserRegisterationForm(request.form)
    if request.method == "POST" and reg_form.validate():
        print(reg_form.uName.data) # get hold of  data input in the field
    return render_template('register.html.j2',render_form = reg_form)