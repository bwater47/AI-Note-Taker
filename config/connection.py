import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Utilize the environment variables
DATABASE_URL = os.getenv('DB_URL', 'postgresql://localhost/notetaker_db')

# Configure the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(bind=engine))

# Base class for models
Base = declarative_base()
