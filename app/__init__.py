from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Som3$ec5etK*y'  # Ideally you'd want this to be a much longer and more random string
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourusername:yourpassword@localhost/databasename'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

# We can also import our config from an object in a separate file.
# This way is a bit better. Ensure you uncomment the import statement
# at the top in addition to the line below.
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import views, models
