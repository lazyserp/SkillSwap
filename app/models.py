from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Hashed password
    skills_offered = db.Column(db.String(200),nullable=True)
    skills_needed = db.Column(db.String(200),nullable=True)
    bio  = db.Column(db.Text,nullable=True)

    