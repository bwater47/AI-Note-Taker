from flask import Blueprint
from .home_routes import home_routes

# Create a blueprint for the main app routes
main_blueprint = Blueprint('main', __name__)

# Register the home_routes blueprint
main_blueprint.register_blueprint(home_routes)
