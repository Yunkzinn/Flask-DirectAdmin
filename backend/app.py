from flask import Flask
from flask_login import LoginManager
from models import db, Users, Article, Jurisprudence, Recommendation

from index import index
from login import login
from logout import logout
from register import register
from home import home
from add_article import add_article
from create_article import create_article
from add_jurisprudence import add_jurisprudence
from create_jurisprudence import create_jurisprudence
from add_recommendation import add_recommendation
from create_recommendation import create_recommendation
from view_article import view_article
from view_jurisprudence import view_jurisprudence
from view_recommendation import view_recommendation

app = Flask(__name__, static_folder='../frontend/static')

# Configurações do aplicativo
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'

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
app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(home)
app.register_blueprint(add_article)
app.register_blueprint(create_article)
app.register_blueprint(add_jurisprudence)
app.register_blueprint(create_jurisprudence)
app.register_blueprint(add_recommendation)
app.register_blueprint(create_recommendation)
app.register_blueprint(view_article)
app.register_blueprint(view_jurisprudence)
app.register_blueprint(view_recommendation)

# Função para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
