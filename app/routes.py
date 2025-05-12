from flask import Blueprint, render_template,redirect,request,url_for,session

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('homepage.html' )


@main.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        user_name = request.form['username']
    return render_template('login.html')


@main.route('/<usr>')
def user(usr):
    return f'Hi,{usr}'