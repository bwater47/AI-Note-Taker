from flask import Blueprint, render_template, jsonify
from models import User, Note

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/', methods=['GET'])
def home():
    try:
        # Get all the notes and join them with the user data
        notes_data = Note.query.join(User).add_columns(Note.id, Note.title, Note.content, User.username).all()
        
        # Serialize the data so the template can read it
        notes = [
            {
                'id': note.id,
                'title': note.title,
                'content': note.content,
                'username': note.username
            }
            for note in notes_data
        ]

        # Render the homepage with notes data
        return render_template('home.handlebars', notes=notes)
    except Exception as e:
        # Handle errors and return a JSON response
        return jsonify({'error': str(e)}), 500