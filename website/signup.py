from flask import Blueprint,  render_template, request, flash, redirect, url_for
from . import db 
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

signup = Blueprint("signup", __name__)


@signup.route("/sign-up", methods =['GET', 'POST'])
def create_new_user():  #this method cannot be the same name as signup because will cause error
  if request.method == 'POST':
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    email_exists = User.query.filter_by(email=email).first()
    username_exists = User.query.filter_by(username=username).first()

    if email_exists:
      flash('Email is already in use', category ='error')
    elif username_exists:
      flash('Username is already in use', category ='error')
    elif password != password2:
      flash('Passwords dont match', category ='error')
    elif len(username) < 2:
      flash('username too short', category = 'error' )  
    elif len(password) < 6:
      flash('Password is too short', category ='error')  
    elif len(email) < 4:
      flash('Email must be greater than 4 characters', category ='error')
    else:
      new_user = User(email=email, username=username, password =generate_password_hash(password, method='sha256') )    
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)
      flash('user created')
      return redirect(url_for('auth.login'))

  return render_template("signup.html")