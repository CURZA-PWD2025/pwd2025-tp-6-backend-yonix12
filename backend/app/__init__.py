from flask import Flask
from flask_cors import CORS  
from ._modulo._routes import modulo_bp

def create_app():
    app = Flask(__name__)
    
    CORS(app)

    app.register_blueprint(modulo_bp)
    return app