from flask import request, jsonify
from models.movie_model import Movie
from schemas.movie_schema import movie_schema, movies_schema
from services.session_scope import session_scope
from flask_jwt_extended import jwt_required

class MovieController:
    @staticmethod
    def get_movies():
        with session_scope() as session:
            movies = session.query(Movie).all()
            return movies_schema.dump(movies), 200

    @staticmethod
    @jwt_required()
    def add_movie():
        data = request.get_json()
        validated_data = movie_schema.load(data)   # Charger et valider les données
        movie = Movie(**validated_data)            # Créer une instance Movie

        with session_scope() as session:
            session.add(movie)
            session.flush()                         # Appliquer les changements pour obtenir l'ID
            return movie_schema.dump(movie), 201

    @staticmethod
    def update_movie(movie_id):
        data = request.get_json()
        with session_scope() as session:
            movie = session.query(Movie).get_or_404(movie_id)
            validated_data = movie_schema.load(data, instance=movie, partial=True)  # Charger et valider les données
            return movie_schema.dump(validated_data), 200

    @staticmethod
    def delete_movie(movie_id):
        with session_scope() as session:
            movie = session.query(Movie).get_or_404(movie_id)
            session.delete(movie)
            return '', 204

    @staticmethod
    def get_movie(movie_id):
        with session_scope() as session:
            movie = session.query(Movie).get_or_404(movie_id)
            return movie_schema.dump(movie), 200
