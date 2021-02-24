from flask.helpers import url_for
from application.users.forms import LoginForm, RegistrationForm, UpdateAccountForm
from flask import Blueprint,flash, redirect, request
from flask.templating import render_template
from application.models import Transaction, User, Post
from application import db, bcrypt
from application.users.utils import upload_to_s3
from flask_login import login_user, logout_user, current_user, login_required
import os


users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/homepage')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now login.', 'success')
        return redirect('/login')
    return render_template('register.html', title = 'Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/homepage')
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/homepage')
        else:
            flash('Failed to log in. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect('/homepage')

@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = upload_to_s3(form.picture.data, os.environ.get('AWS_STORAGE_BUCKET_NAME'))
            current_user.image_file = picture_file
            # current_user.image_file = form.picture.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route('/user/<string:username>/transactions')
def user_transactions(username):
    page = request.args.get('page', type=int)
    user = User.query.filter_by(username=username).first_or_404()
    transactions = Transaction.query.filter_by(creator=user)\
        .order_by(Transaction.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_transactions.html', transactions=transactions, user=user)
