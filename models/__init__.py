from models.User import User
from models.Note import Note
from config.connection import Base, engine

def init_db():
    Base.metadata.drop_all(bind=engine)  # Optional: drops all tables, similar to 'DROP DATABASE'
    Base.metadata.create_all(bind=engine)

__all__ = ['User', 'Note', 'init_db']
