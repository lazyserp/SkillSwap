from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from skillswap_app import db
from skillswap_app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', name="Atul")


@main.route('/home')
def homey():
    username = current_user.username if current_user.is_authenticated else "Guest"
    return render_template('home.html',name=username)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
            return redirect(url_for('main.register'))

        new_user = User(
            username=username,
            password=generate_password_hash(password) )
        
        db.session.add(new_user)
        db.session.commit()
        flash('Registered! Now log in.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid credentials')
            return redirect(url_for('main.login'))

        login_user(user)
        return redirect(url_for('main.home'))

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
