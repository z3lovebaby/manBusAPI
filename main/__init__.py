import os
from flask import Flask
from .user.controller import user
from .extension import db

def create_db(app):
    # Create the database if it doesn't exist
    db_path = os.path.join(os.path.dirname(__file__), "manBus.db")
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Database created at:", db_path)

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    # Check if SQLALCHEMY_DATABASE_URI is set
    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        print("fa")
        raise RuntimeError("Missing SQLALCHEMY_DATABASE_URI")

    # Initialize the database
    db.init_app(app)
    create_db(app)

    # Register blueprints
    app.register_blueprint(user)
    print("App initialized successfully with DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])
    return app
