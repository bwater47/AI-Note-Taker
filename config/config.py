import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Secret Secret Key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or 'mysql+pymysql://root:password@localhost:3306/ai-note-db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False