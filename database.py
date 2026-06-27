from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.get_db_uri()
    db.init_app(app)

def create_tables(app):
    with app.app_context():
        db.create_all()