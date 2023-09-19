from flask import Blueprint,  render_template, request, flash,  redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Details
from flask_login import login_user, logout_user, login_required, current_user
from . import db

update = Blueprint("update", __name__)


@update.route("/update", methods=['GET','POST'])
@login_required
def update_details():
    id = request.form.get('id')
    detail = Details.query.filter_by(id=id).first()
    if request.method == 'POST':
        if detail:
          

          db.session.delete(detail)
          db.session.commit()

          
          full_name = request.form.get('full_name')
          email = request.form.get('email')
          job_title = request.form.get('job_title')
          date_joined = request.form.get('date_joined')
          detail = Details(full_name= full_name, email= email, job_title= job_title, date_joined = date_joined, author= current_user.id)
          db.session.add(detail)
          db.session.commit()
          flash('Details Changed', category = 'success')    
          return redirect(url_for('detailsPage.details'))
        else:
            flash('This id does not exist')
    return render_template('update.html', user=current_user)