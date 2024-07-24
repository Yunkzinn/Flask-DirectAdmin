from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models import db, Article

create_article = Blueprint('create_article', __name__, template_folder='../frontend')

@create_article.route('/create-article', methods=['GET', 'POST'])
@login_required
def show():
    if request.method == 'POST':
        title = request.form.get('title')
        references = request.form.get('references')
        city = request.form.get('city')
        state = request.form.get('state')
        keywords = request.form.get('keywords')
        specialty = request.form.get('specialty')
        content = request.form.get('content')

        new_article = Article(
            title=title,
            references=references,
            city=city,
            state=state,
            keywords=keywords,
            specialty=specialty,  # Campo adicionado
            content=content
        )

        db.session.add(new_article)
        db.session.commit()

        return redirect(url_for('home.articles'))  # Ajuste para a rota correta

    return render_template('create_article.html')
