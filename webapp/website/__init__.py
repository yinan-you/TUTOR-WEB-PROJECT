from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'peepeepoopoo'

    from .views import views
    from .eoi import eoi

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(eoi, url_prefix='/')
    return app