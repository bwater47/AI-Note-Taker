from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app.models import Note
from app import db

note_bp = Blueprint('note', __name__)

@note_bp.route('/note/new', methods=['GET', 'POST'])
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

@note_bp.route('/note/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return render_template('note.html', note=note)

@note_bp.route('/note/<int:id>/delete', methods=['POST'])
@login_required
def delete_note(id):
    note = Note.query.get_or_404(id)
    if note.user_id != current_user.id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    db.session.delete(note)
    db.session.commit()
    return jsonify({'success': True})

@note_bp.route('/note/<int:id>/summarize', methods=['POST'])
@login_required
def summarize_note(id):
    note = Note.query.get_or_404(id)
    if note.user_id != current_user.id:
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    summary_type = request.json.get('summary_type')
    
    # Here, you would integrate with your AI summarization logic
    # For now, we'll just return a placeholder summary
    summary = f"This is a {summary_type} summary of the note: {note.title}"
    
    return jsonify({'success': True, 'summary': summary})