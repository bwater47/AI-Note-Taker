from flask import Flask, render_template
from flask_session import Session
import os
from config.connection import db_session
from models import init_db

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure session
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_SQLALCHEMY'] = db_session.bind
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET')

# Initialize the session
Session(app)

# Initialize the database
init_db()

# Function to close the session after request
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Define routes (controllers)
@app.route('/')
def home():
    return render_template('home.html')  # Use the precompiled HTML template

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 3001)))
