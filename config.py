
import os

class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # DATABASE_URL='postgres://uezvguatemsltd:ff2aa0869fb6ee12b55248b32176b6994c10b1b8e21e8e80f42c3360b96ec78e@ec2-54-90-13-87.compute-1.amazonaws.com:5432/d3cf45ouq7su2'
    
    
    
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
