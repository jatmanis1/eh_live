# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager
# import os
# from .models import db,User,Services
# from flask_cors import CORS
# db = SQLAlchemy()

# from run import db
# migrate = Migrate()
# jwt = JWTManager()

# from .api.task import celery

# def celery()
    
# def create_app():
#     app = Flask(__name__)
#     CORS(app, supports_credentials=True, methods=["GET", "POST", "OPTIONS"])
#     # Load config
#     from config import Config
#     app.config.from_object(Config)

#     # Initialize extensions
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)

#     # Register API routes
#     from .api import initialize_routes
#     initialize_routes(app)

#     # Ensure DB exists
#     db_path = Config.SQLALCHEMY_DATABASE_URI.replace("sqlite:///", "")
#     if not os.path.exists(db_path):
#         with app.app_context():
#             db.create_all()

#     return app





