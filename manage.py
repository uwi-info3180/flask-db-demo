# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app # we import the app object from the app module
from app import db

migrate = Migrate(app, db)
manager = Manager(app) # keeps track of all the commands and handles how they are called from the command line
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run() # prepares your Manager instance to receive input from the command line.