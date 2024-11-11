from main.extension import db
from main.manBus_ma import UserSchema
from main.model import User
from flask import request, jsonify
from sqlalchemy.sql import func
import json
book_schema = UserSchema()
books_schema = UserSchema(many=True)


def add_user_service():
    data = request.json
    print(data)
    if data and ('name' in data) and ('age' in data):
        name = data['name']
        age = data['age']
        try:
            new_book = User(name, age)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add book!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400