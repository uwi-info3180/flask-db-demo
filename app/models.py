from . import db
# from werkzeug.security import generate_password_hash


class User(db.Model):
    # Uncomment the line below if you want to set your own table name
    # __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    #password = db.Column(db.String(255))

    def __init__(self, username, email):
        self.username = username
        self.email = email
        #self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.username
