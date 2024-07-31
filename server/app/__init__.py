from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .models import user, image, video, record
        
        from .routes import auth_routes, record_routes
        
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(record_routes.record_bp)
        
        return app
