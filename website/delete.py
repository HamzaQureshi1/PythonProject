from flask import Blueprint,  render_template, request, flash,  redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Details
from flask_login import login_user, logout_user, login_required, current_user
from . import db

delete = Blueprint("delete", __name__)

@login_required
@delete.route('/delete', methods=['GET','POST'])
def remove():
    id = request.form.get('id')
    detail = Details.query.filter_by(id=id).first()
    if request.method == 'POST':
        if detail:
            db.session.delete(detail)
            db.session.commit()
            return redirect(url_for('detailsPage.details'))
 
    return render_template('delete.html')