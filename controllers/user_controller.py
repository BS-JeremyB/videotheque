from flask import request, jsonify
from models.user_model import User
from schemas.user_schema import user_schema
from services.session_scope import session_scope
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        validated_data = user_schema.load(data)  # Charger et valider les données
        hashed_password = generate_password_hash(validated_data['password'])
        
        user = User(username=validated_data['username'], email=validated_data['email'], password_hash=hashed_password)

        with session_scope() as session:
            session.add(user)
            return user_schema.dump(user), 201

    @staticmethod
    def login_user():
        data = request.get_json()
        with session_scope() as session:
            user = session.query(User).filter_by(username=data['username']).first()
            if user and check_password_hash(user.password_hash, data['password']):
                access_token = create_access_token(identity=user.id)
                return jsonify(access_token=access_token), 200
            return jsonify(message="Invalid credentials"), 401
