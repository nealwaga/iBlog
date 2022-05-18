import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'
    SQLALCHEMY_DATABASE_URI = 'postgres://kvniowexaemmua:78578deba5ffba2bbf019a9969cbbbea241bb9f8c9f626a3578efeaad3348fe1@ec2-52-86-115-245.compute-1.amazonaws.com:5432/d1cf50sk6jl424'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_USERNAME = 'waganeal@gmail.com'
    MAIL_PASSWORD = 'wnScrumhalf9.'
    SUBJECT_PREFIX = 'iBlog.com'
    SENDER_EMAIL = 'waganeal@gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'


class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'
    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri and uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    #rest of connection code using the connection string `uri`
    SQLALCHEMY_DATABASE_URI=uri

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
