from flask import Flask
from flask_migrate import Migrate
from app import db  
from app.routes.auth_routes import auth_bp
from app.routes.record_routes import record_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Ireporter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  
migrate = Migrate(app, db)  

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(record_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
