import os
from flask import Flask
from flask_login import LoginManager
from .models import db, Users, Article

def create_app():
    app = Flask(__name__, static_folder='../frontend/static')

    # Configurações do aplicativo
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

    # Configuração do banco de dados
    if 'DATABASE_URL' in os.environ:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../backend/database.db'

    # Configuração do LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'login.show'  # Nome da view de login
    login_manager.init_app(app)

    # Inicialização do banco de dados
    db.init_app(app)

    # Criação das tabelas se não existirem
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

    # Registro dos Blueprints
    from .index import index
    from .login import login
    from .logout import logout
    from .register import register
    from .home import home
    from .add_article import add_article
    from .create_article import create_article
    from .add_jurisprudence import add_jurisprudence
    from .create_jurisprudence import create_jurisprudence
    from .view_article import view_article
    from .view_jurisprudence import view_jurisprudence

    app.register_blueprint(index)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(register)
    app.register_blueprint(home)
    app.register_blueprint(add_article)
    app.register_blueprint(create_article)
    app.register_blueprint(add_jurisprudence)
    app.register_blueprint(create_jurisprudence)
    app.register_blueprint(view_article)
    app.register_blueprint(view_jurisprudence)

    # Função para carregar o usuário
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app
