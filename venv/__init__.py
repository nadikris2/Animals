from flask import Flask
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy, event
from os import path
from sqlalchemy.sql.expression import desc  
from flask_login import LoginManager,UserMixin, current_user

db = SQLAlchemy()
UPLOAD_FOLDER = 'static/image'



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '321800014'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/pos'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)

    from venv.views import views
    from venv.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User


    login = LoginManager(app)


    @login.user_loader
    def load_user(id):
        user = User.query.filter_by(id=id).first()
        return user

    return app


