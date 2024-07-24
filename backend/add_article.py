from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Article

add_article = Blueprint('add_article', __name__, template_folder='../frontend')

@add_article.route('/home/articles')
def show():
    articles = Article.query.all()
    return render_template('articles.html', articles=articles)

@add_article.route('/home/edit-article/<int:id>', methods=['GET', 'POST'])
def edit_article(id):
    article = Article.query.get_or_404(id)
    
    if request.method == 'POST':
        article.title = request.form['title']
        article.references = request.form['references']
        article.city = request.form['city']
        article.state = request.form['state']
        article.keywords = request.form['keywords']
        article.content = request.form['content']
        
        db.session.commit()
        return redirect(url_for('add_article.show'))
    
    return render_template('edit_article.html', article=article)

@add_article.route('/home/delete-article/<int:id>', methods=['POST'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('add_article.show'))
