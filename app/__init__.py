from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import os
from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")  # or MySQL URI
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
