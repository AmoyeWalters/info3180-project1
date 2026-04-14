import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///lab5.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False