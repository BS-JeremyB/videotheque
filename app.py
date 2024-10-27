from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager  # Gestion de session utilisateur pour les templates
from flask_jwt_extended import JWTManager  # Pour l'authentification par JWT
from config import Config
from services.jwt_management import initialize_jwt

# Initialisation de l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialisation des extensions
db = SQLAlchemy(app)             # Gestion de la base de données
migrate = Migrate(app, db)       # Migration de la base de données
jwt = JWTManager(app)            # Gestion des tokens JWT

# Initialisation du LoginManager pour la gestion des sessions utilisateur
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Page de login pour les routes protégées via login_required

# Charger l'utilisateur depuis la base de données pour Flask-Login
from models.user_model import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importation des blueprints (routes) pour l'API et les templates
from routes.movie_routes import movie_api_bp, movie_bp
from routes.director_routes import director_api_bp, director_bp
from routes.auth_routes import auth_bp, auth_api_bp
from routes.main_routes import main_bp

# Enregistrement des blueprints
app.register_blueprint(main_bp)                      # Routes de templates principales
app.register_blueprint(movie_bp)                      # Routes de templates pour les films
app.register_blueprint(movie_api_bp, url_prefix='/api')  # Routes API pour les films
app.register_blueprint(director_bp)                   # Routes de templates pour les réalisateurs
app.register_blueprint(director_api_bp, url_prefix='/api')  # Routes API pour les réalisateurs
app.register_blueprint(auth_bp, url_prefix='/auth')   # Routes pour l'authentification et l'API utilisateur
app.register_blueprint(auth_api_bp, url_prefix='/api')   # Routes API pour l'authentification utilisateur

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run()
