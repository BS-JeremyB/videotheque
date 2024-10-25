from flask import Blueprint, render_template, redirect, url_for
from app import db
from forms.movie_form import MovieForm
from models.movie_model import Movie
from services.session_scope import session_scope
from flask_login import login_required

movie_bp = Blueprint('movies', __name__)

@movie_bp.route('/movies', methods=['GET'])
def list_movies():
    with session_scope() as session:
        movies = session.query(Movie).all()
    return render_template('list_movies.html', movies=movies)

@movie_bp.route('/movie/add', methods=['GET', 'POST'])
@login_required
def add_movie():
    form = MovieForm()
    form.populate_director_choices()
    if form.validate_on_submit():
        new_movie = Movie(title=form.title.data, director_id=form.director_id.data)
        with session_scope() as session:
            session.add(new_movie)
        return redirect(url_for('movies.list_movies'))
    return render_template('add_movie.html', form=form)
