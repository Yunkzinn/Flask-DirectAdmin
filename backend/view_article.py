from flask import Blueprint, render_template
from models import Article

view_article = Blueprint('view_article', __name__)

@view_article.route('/view-article/<int:id>')
def show(id):
    article = Article.query.get_or_404(id)
    return render_template('view_article.html', article=article)
