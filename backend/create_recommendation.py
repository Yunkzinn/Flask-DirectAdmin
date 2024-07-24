from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import db, Recommendation
import os

create_recommendation = Blueprint('create_recommendation', __name__, template_folder=os.path.abspath('../frontend'))

@create_recommendation.route('/create-recommendation', methods=['GET', 'POST'])
@login_required
def show():
    if request.method == 'POST':
        theme = request.form['theme']
        recommendations = request.form['recommendations']
        keywords = request.form['keywords']
        specialty = request.form['specialty']
        content = request.form['content']
        
        new_recommendation = Recommendation(
            theme=theme,
            recommendations=recommendations,
            keywords=keywords,
            specialty=specialty,
            content=content
        )
        
        db.session.add(new_recommendation)
        db.session.commit()
        
        return redirect(url_for('add_recommendation.show'))  # Ajuste para a rota correta

    return render_template('create_recommendation.html')  # Corrigir o nome do template aqui
