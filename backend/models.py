from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    references = db.Column(db.String(300))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    keywords = db.Column(db.String(200))
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Article {self.title}>'

class Jurisprudence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    references = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    keywords = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Jurisprudence {self.title}>'
