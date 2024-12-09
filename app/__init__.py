import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar extensiones
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///pagos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)

    return app
