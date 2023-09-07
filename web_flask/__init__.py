from flask import Flask
from flask_login import LoginManager
from datetime import timedelta
from models import storage


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'famec'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=3600)  # Set session timeout to 1 hour
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=3600)  # Set the duration you want here

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return storage.find_user_by_id(id)

    # Define the custom filter function
    def enum_to_string(enum_value):
        return str(enum_value).split('.')[-1]
    # Register the custom filter in the Flask app
    app.jinja_env.filters['enum_to_string'] = enum_to_string


    return app

def configure_db(app):
    with app.app_context():
        storage.reload()
    return app
