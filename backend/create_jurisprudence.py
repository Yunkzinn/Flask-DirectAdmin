from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Jurisprudence
import os

create_jurisprudence = Blueprint('create_jurisprudence', __name__, template_folder=os.path.abspath('../frontend'))

@create_jurisprudence.route('/create-jurisprudence', methods=['GET', 'POST'])
@login_required
def show():
    if request.method == 'POST':
        title = request.form['title']
        references = request.form['references']
        city = request.form['city']
        state = request.form['state']
        keywords = request.form['keywords']
        content = request.form['content']
        
        new_jurisprudence = Jurisprudence(
            title=title,
            references=references,
            city=city,
            state=state,
            keywords=keywords,
            content=content
        )
        
        db.session.add(new_jurisprudence)
        db.session.commit()
        
        return redirect(url_for('home.jurisprudences'))  # Ajuste para a rota correta

    return render_template('create_jurisprudence.html')  # Corrigir o nome do template aqui
