from flask import Blueprint,  render_template, request, flash, redirect, url_for
from . import db 
from .models import User, Details
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

detailsPage = Blueprint("detailsPage", __name__)

@detailsPage.route("/detailsPage")
@login_required
# This function pulls data from the details table in the database and passes if to the details html file where the content will be displayed.
def details():
  details = Details.query.all()
  return render_template("details.html", user = current_user,details=details)

