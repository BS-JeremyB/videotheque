
# Videotheque Project

Ce projet est une application Flask pour gérer une vidéothèque, permettant d'ajouter et de visualiser des films et des réalisateurs. Le projet inclut désormais une API RESTful pour accéder et manipuler les données via des endpoints JSON, ainsi qu'une gestion des utilisateurs avec authentification JWT.

## Prérequis

- Python 3.x
- PostgreSQL (pour la base de données)

## Installation

1. **Cloner le projet** :
   ```bash
   git clone <url-du-projet>
   cd videotheque
   ```

2. **Créer un environnement virtuel et activer-le** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Linux/Mac
   venv\Scripts\activate  # Sur Windows
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données et les variables d'environnement** :
   Créez un fichier `.env` dans le dossier racine avec les variables de configuration nécessaires :
   ```env
   SECRET_KEY=your_secret_key
   JWT_SECRET_KEY=your_jwt_secret_key
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/dbname
   ```

5. **Initialiser la base de données** :
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Lancer l'application

Pour lancer l'application, exécutez la commande suivante :
```bash
flask run
```

L'application sera accessible à `http://localhost:5000`.

## Utilisation de l'API

L'API RESTful est accessible via le préfixe `/api`. Voici un aperçu des endpoints principaux :

### Endpoints Films

- **GET /api/movies** : Récupère la liste de tous les films.
- **POST /api/movies** : Ajoute un nouveau film (nécessite un JWT pour l'authentification).
- **PUT /api/movies/<movie_id>** : Modifie un film existant.
- **DELETE /api/movies/<movie_id>** : Supprime un film existant.

### Endpoints Réalisateurs

- **GET /api/directors** : Récupère la liste de tous les réalisateurs.
- **POST /api/directors** : Ajoute un nouveau réalisateur.

### Endpoints Utilisateurs

- **POST /auth/register** : Enregistre un nouvel utilisateur.
- **POST /auth/login** : Connecte un utilisateur et retourne un token JWT.

## Authentification JWT

Certaines routes de l'API, comme `POST /api/movies`, nécessitent un token JWT pour authentifier l'utilisateur. Pour obtenir un token JWT :
1. Utilisez l'endpoint **POST /auth/login** pour vous connecter en fournissant `username` et `password`.
2. Ajoutez le token JWT reçu dans les en-têtes des requêtes pour les routes nécessitant une authentification :
   ```
   Authorization: Bearer <your_token>
   ```

## Dépendances supplémentaires

Les nouvelles dépendances pour la gestion de l'API et des tokens JWT sont :
- `Flask-JWT-Extended` : pour gérer l'authentification JWT.
- `Marshmallow` : pour la sérialisation et désérialisation des données JSON.

## Tests

Pour exécuter les tests :
```bash
pytest
```

## Migrations

Pour gérer les migrations de base de données (après avoir modifié les modèles) :
```bash
flask db migrate -m "Description de la migration"
flask db upgrade
```

---

Ce fichier `README.md` fournit les informations de base sur l'installation, l'utilisation de l'API, l'authentification JWT, et les nouvelles dépendances pour le projet Videotheque.
