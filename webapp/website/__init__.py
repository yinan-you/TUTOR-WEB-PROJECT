from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = 'peepeepoopoo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .join_front_page import join_front_page

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(join_front_page, url_prefix='/')

    from website.models import User, Note

    create_database(app)

    return app


def create_database(app):
    with app.app_context():  # Activate the app context
        if not path.exists('website/' + DB_NAME):  # Check if the database exists
            print("Creating database...")
            db.create_all()  # No 'app' argument is needed here
            print("Database created!")
        else:
            print("Database already exists.")