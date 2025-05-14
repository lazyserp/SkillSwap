from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import RegisterForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template("homepage.html.j2")

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.uPass.data)

        new_user = User(
            name=form.uName.data,
            dob=form.uDob.data,
            gender=form.uGender.data,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully!", "success")
        return redirect(url_for('main.login'))

    return render_template("register.html.j2", render_form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html.j2")
