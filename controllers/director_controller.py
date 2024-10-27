from flask import request, jsonify
from models.director_model import Director
from schemas.director_schema import director_schema, directors_schema
from services.session_scope import session_scope

class DirectorController:
    @staticmethod
    def list_directors():
        with session_scope() as session:
            directors = session.query(Director).all()
            return directors_schema.dump(directors), 200

    @staticmethod
    def add_director():
        data = request.get_json()
        validated_data = director_schema.load(data)  # Charger et valider les données
        director = Director(**validated_data)        # Créer une instance Director

        with session_scope() as session:
            session.add(director)
            return director_schema.dump(director), 201
