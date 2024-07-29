from app import db

def init_db():
    # No need for subtransactions here
    db.drop_all()  # Optional: drops all tables
    db.create_all()  # Create all tables

__all__ = ['init_db']
