from os import getenv
from dotenv import load_dotenv

load_dotenv()
class Config:
    """ Set Flask configuration vars from .env file """

    #General Configs
    TESTING = getenv('TESTING')
    FLASK_DEBUG = getenv('FLASK_DEBUG')
    #SECRET_KEY = environ.get('SECRET_KEY')

    #Database
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    