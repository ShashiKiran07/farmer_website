import click
from flask.cli import with_appcontext

from application import db
from .models import User, Post, Transaction

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()