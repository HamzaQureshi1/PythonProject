from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  username = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  date_created = db.Column(db.DateTime(timezone = True), default = func.now())
  admin = db.Column(db.Integer, unique=True)


class Details(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String(150), unique=True)
  email = db.Column(db.String(150), unique=True)
  job_title = db.Column(db.String(150), unique=True)
  date_joined = db.Column(db.String(150), unique = True)
  author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = "CASCADE"), nullable = False)