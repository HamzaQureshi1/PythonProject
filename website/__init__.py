from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "helloworld" # secret key is used to encrypt or hash session data
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)


  from .auth import auth
  from .detailsPage import detailsPage
  from .signup import signup
  from .update import update
  from .delete import delete
  from .models import User, Details

  app.register_blueprint(auth, url_prefix="/")
  app.register_blueprint(detailsPage, url_prefix="/")
  app.register_blueprint(signup, url_prefix="/")
  app.register_blueprint(update, url_prefix="/")
  app.register_blueprint(delete, url_prefix="/")

  login_manager = LoginManager()
  login_manager.login_view = "auth.login"  #where to redirect if user is not logged in 
  login_manager.init_app(app)

  def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
          db.create_all()
        print("Created database!")

  create_database(app)

  @login_manager.user_loader
  def load_user(id): 
    return User.query.get(int(id)) #login manager uses a session to store id of user to login.  This id is used to access info for login of that user. we are defining how we will access the user given the id.

  return app
