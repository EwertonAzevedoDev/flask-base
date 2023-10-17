from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt 
from config import Config

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    bcrypt.init_app(app)

    from .views import views
    from .auth import auth
    from .protected_views import protected_views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(protected_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app