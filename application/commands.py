import click
from flask.cli import with_appcontext

from application import db, create_app
from .models import User, Post, Transaction

app = create_app

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    with app.app_context():
        db.create_all()