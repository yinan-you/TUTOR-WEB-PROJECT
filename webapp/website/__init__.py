from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'peepeepoopoo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite///{DB_NAME}'

    from .views import views
    from .eoi import eoi

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(eoi, url_prefix='/')
    return app