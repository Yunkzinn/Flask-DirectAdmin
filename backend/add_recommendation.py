from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Recommendation

add_recommendation = Blueprint('add_recommendation', __name__, template_folder='../frontend')

@add_recommendation.route('/home/recommendations')
def show():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    sort_by = request.args.get('sort_by', 'theme_asc')

    if sort_by == 'theme_asc':
        order = Recommendation.theme.asc()
    elif sort_by == 'theme_desc':
        order = Recommendation.theme.desc()
    elif sort_by == 'date_asc':
        order = Recommendation.created_at.asc()
    elif sort_by == 'date_desc':
        order = Recommendation.created_at.desc()
    else:
        order = Recommendation.theme.asc()  # Ordenação padrão

    recommendations = Recommendation.query.order_by(order).paginate(page=page, per_page=per_page)

    return render_template('recommendations.html', recommendations=recommendations, sort_by=sort_by)

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
        return redirect(url_for('add_recommendation.show', page=1))
    
    return render_template('edit_recommendation.html', recommendation=recommendation)

@add_recommendation.route('/home/delete-recommendation/<int:id>', methods=['POST'])
def delete_recommendation(id):
    recommendation = Recommendation.query.get_or_404(id)
    db.session.delete(recommendation)
    db.session.commit()
    return redirect(url_for('add_recommendation.show', page=1))
