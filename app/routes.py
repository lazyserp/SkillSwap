from flask import Blueprint, render_template,redirect

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('homepage.html' )


@main.route('/login')
def login():
    return render_template('login.html')