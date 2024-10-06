from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app import Note
from app import db

bp = Blueprint('note', __name__)

@bp.route('/note/new', methods=['GET', 'POST'])
@login_required
def new_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_note = Note(title=title, content=content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return render_template('note.html')

@bp.route('/note/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return render_template('note.html', note=note)

@bp.route('/note/<int:id>/delete', methods=['POST'])
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('dashboard.index'))

@bp.route('/note/<int:id>/summarize', methods=['POST'])
@login_required
def summarize_note(id):
    note = Note.query.get_or_404(id)
    summary_type = request.form.get('summary_type')
    # Here you would integrate with your AI summarization logic
    # For now, we'll just return a placeholder
    summary = f"This is a {summary_type} summary of '{note.title}'"
    return jsonify({'summary': summary})