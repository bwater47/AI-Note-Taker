from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import Note

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required
def index():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', notes=notes)