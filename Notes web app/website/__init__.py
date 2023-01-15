from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize database 
# db is object of database which we used to store delete perform all database related operations
db = SQLAlchemy() 
DB_NAME = "notes.database.db"

def create_app():
    app = Flask(__name__)
    # Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering
    # app.config['SECRET_KEY'] = 'abahsvsgdvch'

    # Database is located at f'sqlite://{DB_NAME}' this location
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # The application context keeps track of the application-level data during a request, 
    # CLI command, or other activity. Rather than passing the application around to each function,
    # the current_app and g proxies are accessed instead.
    with app.app_context():
        app.config['SECRET_KEY'] = 'abahsvsgdvch'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        db.init_app(app)
    
    
        from .views import views
        from .auth import auth
        
        app.register_blueprint(views,url_prefix='/')
        app.register_blueprint(auth,url_prefix='/')
        
        from .models import User, Note
        create_database()
        
        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)
        
        return app

def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Database Created')