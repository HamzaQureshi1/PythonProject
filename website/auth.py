from flask import Blueprint,  render_template, request, flash,  redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Details
from flask_login import login_user, logout_user, login_required, current_user
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.login'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")

@auth.route("/post", methods=['GET','POST'])
@login_required
def create_post():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        job_title = request.form.get('job_title')
        date_joined = request.form.get('date_joined')

        if not full_name and email and job_title and date_joined:
            flash('All details required to add new employee', category='error')
        else:
            detail = Details(full_name= full_name, email= email, job_title= job_title, date_joined = date_joined, author= current_user.id)
            db.session.add(detail)
            db.session.commit()
            flash('Details added', category = 'success')    
            return redirect(url_for('detailsPage.details'))
    return render_template('post.html', user=current_user)

@auth.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("auth.login")) 