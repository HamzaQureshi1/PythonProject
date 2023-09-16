from flask import Blueprint,  render_template, request, flash, redirect, url_for
from . import db 
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

detailsPage = Blueprint("detailsPage", __name__)

@detailsPage.route("/detailsPage")
def details():
  return render_template("details.html", name = "Hamza")

@detailsPage.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("detailsPage.details")) 