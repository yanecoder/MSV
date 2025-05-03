from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    from .routes import main, send, get
    app.register_blueprint(main)
    app.register_blueprint(send)
    app.register_blueprint(get)

    
    with app.app_context():
        db.create_all()
        
    return app