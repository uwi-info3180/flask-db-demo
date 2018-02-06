from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yourusername:yourpassword@localhost/databasename'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
db = SQLAlchemy(app)

from app import views, models