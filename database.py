from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


# conf de migração
migrate = Migrate()

db = SQLAlchemy()
load_dotenv()


def create_app():
    # Criar a instância do Flask
    app = Flask(__name__)

    # Define a URL do banco de dados com base nas variáveis de ambiente
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Registrar a extensão SQLAlchemy no aplicativo Flask
    migrate.init_app(app, db)  # Inicializar a extensão de migração

    return app
