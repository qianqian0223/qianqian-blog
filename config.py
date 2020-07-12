class Config(object):
    """Base config class."""
    SECRET_KEY = '2088d15f95dd7d56322afd9b699e00e3'
    

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:123456@127.0.0.1:3306/qianblog'


