from flask import Blueprint, render_template, request
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
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Obter o parâmetro de ordenação da URL
    sort_by = request.args.get('sort_by', 'title_asc')

    # Configurar a ordenação com base no parâmetro
    if sort_by == 'title_asc':
        order = Jurisprudence.title.asc()
    elif sort_by == 'title_desc':
        order = Jurisprudence.title.desc()
    elif sort_by == 'date_asc':
        order = Jurisprudence.created_at.asc()
    elif sort_by == 'date_desc':
        order = Jurisprudence.created_at.desc()
    else:
        order = Jurisprudence.title.asc()  # Ordenação padrão

    jurisprudences = Jurisprudence.query.order_by(order).paginate(page=page, per_page=per_page)

    return render_template('jurisprudences.html', jurisprudences=jurisprudences, sort_by=sort_by)
