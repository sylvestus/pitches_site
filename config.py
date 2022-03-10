
import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # DATABASE_URL='postgresql://eylkaaumgmaavp:8d84eee8ca2c9368d2095e8baff1d029e1d87945cd8b256f64ae2adfb45f8a50@ec2-52-73-149-159.compute-1.amazonaws.com:5432/d3ndrpmoifj04j'
    
    #email configurations
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'silvanussigei19960@gmail.com'
    MAIL_PASSWORD = 'Id34306488'

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI').replace("://", "ql://", 1)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig  
}
