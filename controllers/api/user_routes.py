from flask import Blueprint, request, jsonify
from models.user import User
from config.connection import db_session

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db_session.add(new_user)
        db_session.commit()
        return jsonify({
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email
        }), 200
    except Exception as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 400
