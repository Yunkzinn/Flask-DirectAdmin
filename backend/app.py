from flask import Flask, jsonify, request
from flask_login import LoginManager, login_required
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from models import db, Users, Article, Jurisprudence, Recommendation
import datetime

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
app.config['SECRET_KEY'] = 'your_flask_secret_key'  # Substitua por uma chave secreta forte
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
app.config['JWT_SECRET_KEY'] = 'my_very_secret_jwt_key'  # JWT Token que você vai gerar e manter seguro
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # Token JWT nunca expira

# Configuração do JWT
jwt = JWTManager(app)

# Configuração do LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login.show'  # Nome da view de login
login_manager.init_app(app)

# Configuração do Rate Limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

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

# Rota para consultar Jurisprudencias
@app.route('/api/jurisprudencias', methods=['GET'])
@jwt_required()
@limiter.limit("10 per minute")
def get_jurisprudencias():
    jurisprudencias = Jurisprudence.query.all()
    results = [
        {
            "id": j.id,
            "title": j.title,
            "references": j.references,
            "city": j.city,
            "state": j.state,
            "keywords": j.keywords,
            "specialty": j.specialty,
            "content": j.content
        } for j in jurisprudencias]
    return jsonify(results)

# Rota para consultar Artigos
@app.route('/api/artigos', methods=['GET'])
@jwt_required()
@limiter.limit("10 per minute")
def get_artigos():
    artigos = Article.query.all()
    results = [
        {
            "id": a.id,
            "title": a.title,
            "references": a.references,
            "city": a.city,
            "state": a.state,
            "keywords": a.keywords,
            "specialty": a.specialty,
            "categoria": a.categoria,  # Campo adicionado
            "content": a.content
        } for a in artigos]
    return jsonify(results)

# Rota para consultar Recomendacoes
@app.route('/api/recomendacoes', methods=['GET'])
@jwt_required()
@limiter.limit("10 per minute")
def get_recomendacoes():
    recomendacoes = Recommendation.query.all()
    results = [
        {
            "id": r.id,
            "theme": r.theme,
            "recommendations": r.recommendations,
            "keywords": r.keywords,
            "specialty": r.specialty,
            "content": r.content
        } for r in recomendacoes]
    return jsonify(results)

# Rota para gerar um novo token JWT (apenas para usuários logados)
@app.route('/generate_token', methods=['GET'])
@login_required  # Protege a rota para que apenas usuários autenticados possam acessá-la
def generate_token():
    identity = 'user_id_or_identifier'  # Identidade do usuário ou outra identificação
    token = create_access_token(identity=identity)
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
