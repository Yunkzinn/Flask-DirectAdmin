from flask import Blueprint, render_template
from models import Recommendation

view_recommendation = Blueprint('view_recommendation', __name__)

@view_recommendation.route('/view-recommendation/<int:id>')
def show(id):
    recommendation = Recommendation.query.get_or_404(id)
    return render_template('view_recommendation.html', recommendation=recommendation)
