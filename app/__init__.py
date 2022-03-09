from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import sqlalchemy
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE





login_manager = LoginManager()
login_manager.session_protection= 'strong'
login_manager.login_view='auth.login'

bootstrap=Bootstrap()
db = SQLAlchemy()

photos =UploadSet('photos',IMAGES)


mail= Mail()
simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLAlchemy_TRACK_MODIFICATIONS']=False
    app.config['DATABASE_URI']='postgres://syrcqodnxxjfjx:2d9595580c7827528afbb2e849c8416fde370ca3f30056f14ba274286a849d4c@ec2-44-192-245-97.compute-1.amazonaws.com:5432/ds34ma9sk630j'

    # configure UploadSet
    configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    
   

    #Registering the blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint,url_prefix = '/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    #setting config
    # from .requests import configure_request
    # configure_request(app)

    return app


