import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///vehicles.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
