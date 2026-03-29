import os

class Config:
    # Set the base directory to the folder where this file is located
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Basic SQLite database setup
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
