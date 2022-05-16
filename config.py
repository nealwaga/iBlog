import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = 
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neal:Wneal9.@localhost/blogs'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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
