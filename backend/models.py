from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    specialty = db.Column(db.String(100))  # Campo adicionado
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
    specialty = db.Column(db.String(100))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Novo campo

    def __repr__(self):
        return f'<Jurisprudence {self.title}>'

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(150), nullable=False)
    recommendations = db.Column(db.String(300))
    keywords = db.Column(db.String(255))
    specialty = db.Column(db.String(100))
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Recommendation {self.theme}>'
