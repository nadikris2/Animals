from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import  User, requires_roles
from . import db
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
	return render_template('index.html')

@auth.route('/login/', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('auth.home'))
	
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		
		if user is None:
			flash('Invalid username')
			return redirect(url_for('auth.login'))

		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('auth.home'))
	return render_template('login.html', title='Sign In', form=form)

@auth.route('/register/', methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = RegistrationForm()
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		role = form.role.data
		user = User(username=username, email=email, role=role);
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('auth.login'))
	return render_template('register.html', title='Register', form=form)



@auth.route('/logout/')
@login_required
@requires_roles('admin','customer')
def logout():
    logout_user()
    return redirect(url_for('auth.home'))



