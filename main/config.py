import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/manBus.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False