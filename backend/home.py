from flask import Blueprint, render_template
from flask_login import login_required
from models import Article, Jurisprudence
import os

home = Blueprint('home', __name__, template_folder=os.path.abspath('../frontend'))

@home.route('/home/articles', methods=['GET'])
@login_required
def articles():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@home.route('/home/jurisprudences', methods=['GET'])
@login_required
def jurisprudences():
    jurisprudences = Jurisprudence.query.all()
    return render_template('jurisprudences.html', jurisprudences=jurisprudences)  # Corrigir o nome do template aqui
