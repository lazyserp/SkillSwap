from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aman'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skillswap.db'

    db.init_app(app)
    login_manager.init_app(app)

    from skillswap_app.models import User  # 🔄 use full package name
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from skillswap_app.routes import main
    app.register_blueprint(main)

    return app
