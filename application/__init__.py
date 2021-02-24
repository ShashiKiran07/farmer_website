import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from application.config import Config
from flask_admin import Admin
import boto3
from flask_s3 import FlaskS3

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
admin = Admin()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
s3 = FlaskS3()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    app.config['AWS_ACCESS_KEY_ID'] = os.environ.get('AWS_ACCESS_KEY_ID')
    app.config['AWS_SECRET_ACCESS_KEY'] = os.environ.get('AWS_SECRET_ACCESS_KEY')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    s3.init_app(app)
    
    from application.models import User, Post, Transaction, MyModelView
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Post, db.session))
    admin.add_view(MyModelView(Transaction, db.session))

    from application.users.routes import users
    from application.posts.routes import posts
    from application.main.routes import main
    from application.transactions.routes import transactions
    from application.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(transactions)
    app.register_blueprint(errors)


    return app

