from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
db = SQLAlchemy()

# Configure Flask-Session
session = Session()