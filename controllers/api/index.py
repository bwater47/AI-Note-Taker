from flask import Blueprint

# Import route blueprints
from .user_routes import user_routes

# Create a blueprint for the API
api_blueprint = Blueprint('api', __name__)

# Register blueprints
api_blueprint.register_blueprint(user_routes, url_prefix='/users')

# Add more route blueprints here if needed
# from .another_routes import another_routes
# api_blueprint.register_blueprint(another_routes, url_prefix='/another')
