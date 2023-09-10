from flask import Blueprint, render_template

detailsPage = Blueprint("detailsPage", __name__)

@detailsPage.route("/detailsPage")
def details():
  return render_template("details.html")