from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from werkzeug.security import generate_password_hash, check_password_hash
from config.connection import Base, engine

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    notes = relationship('Note', back_populates='user', cascade='all, delete')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 8
        return generate_password_hash(password)
