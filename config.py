import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'
    #SQLALCHEMY_DATABASE_URI = 'postgres://gkcqkszsaludeg:52eb94e487f0210f566752efc416c41a7f43800dac508debfa0fb05418d466ba@ec2-44-195-169-163.compute-1.amazonaws.com:5432/d9am8t1lgh2lu8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '7Q6itHDJ6LqJMTKWDM5SCjGwQDQurh'
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
