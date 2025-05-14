from flask import Blueprint, render_template, redirect, url_for, flash,session,request
from app.forms import RegisterForm,LoginForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash,check_password_hash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template("homepage.html.j2")

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.uPass.data)
        skills_offered = form.skills_offered.data
        skills_needed = form.skills_needed.data
        bio  = form.bio.data

        new_user = User( 
            name=form.uName.data,
            dob=form.uDob.data,
            gender=form.uGender.data,
            password=hashed_password,
            skills_offered = skills_offered,
            skills_needed = skills_needed,
            bio = bio )

        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully!", "success")
        return redirect(url_for('main.login'))

    return render_template("register.html.j2", render_form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():  # ✅ MUST be there!
        user = User.query.filter_by(name=form.uName.data).first()
        if user and check_password_hash(user.password, form.uPass.data):
            session["user_id"] = user.id
            flash(f"Welcome back, {user.name}!", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html.j2", form=form)



@main.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("Please Log in first,","warning")
        return redirect(url_for("main.login"))
    
    user = User.query.get(session["user_id"])
    return render_template("dashboard.html.j2",user=user)

@main.route('/logout')
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully.", "info")
    return redirect(url_for("main.login"))
