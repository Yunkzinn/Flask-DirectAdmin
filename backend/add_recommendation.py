from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Recommendation

add_recommendation = Blueprint('add_recommendation', __name__, template_folder='../frontend')

@add_recommendation.route('/home/recommendations')
def show():
    recommendations = Recommendation.query.all()
    return render_template('recommendations.html', recommendations=recommendations)

@add_recommendation.route('/home/edit-recommendation/<int:id>', methods=['GET', 'POST'])
def edit_recommendation(id):
    recommendation = Recommendation.query.get_or_404(id)
    
    if request.method == 'POST':
        recommendation.theme = request.form['theme']
        recommendation.recommendations = request.form['recommendations']
        recommendation.keywords = request.form['keywords']
        recommendation.specialty = request.form['specialty']
        recommendation.content = request.form['content']
        
        db.session.commit()
        return redirect(url_for('add_recommendation.show'))
    
    return render_template('edit_recommendation.html', recommendation=recommendation)

@add_recommendation.route('/home/delete-recommendation/<int:id>', methods=['POST'])
def delete_recommendation(id):
    recommendation = Recommendation.query.get_or_404(id)
    db.session.delete(recommendation)
    db.session.commit()
    return redirect(url_for('add_recommendation.show'))
