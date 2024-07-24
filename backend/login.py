from flask import Blueprint, url_for, render_template, redirect, request
from flask_login import login_user
from werkzeug.security import check_password_hash

from models import Users

login = Blueprint('login', __name__, template_folder='../frontend')

@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home.articles'))  # Redireciona para /home/articles
        else:
            return redirect(url_for('login.show') + '?error=incorrect-password')
    else:
        return render_template('login.html')
