from flask import Blueprint, render_template
from models import Jurisprudence  # Certifique-se de que a classe Jurisprudence está definida em models.py

view_jurisprudence = Blueprint('view_jurisprudence', __name__)

@view_jurisprudence.route('/view-jurisprudence/<int:id>')
def show(id):
    jurisprudence = Jurisprudence.query.get_or_404(id)
    return render_template('view_jurisprudence.html', jurisprudence=jurisprudence)
