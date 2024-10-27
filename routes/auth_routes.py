from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from models.user_model import User
from forms.register_form import RegistrationForm
from forms.login_form import LoginForm
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from controllers.user_controller import UserController

# Blueprint pour les routes d'authentification API (JSON responses)
auth_api_bp = Blueprint('auth_api', __name__)

# Routes API
auth_api_bp.route('/register', methods=['POST'])(UserController.register_user)
auth_api_bp.route('/login', methods=['POST'])(UserController.login_user)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Registration successful', 'success')
        return redirect(url_for('main.home'))
    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))