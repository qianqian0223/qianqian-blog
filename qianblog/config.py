class Config(object):
    """Base config class."""
    # WTForm secret key
    SECRET_KEY = 'WTForms key'
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6Lc7ebAZAAAAABnFMbhL2U2o4GwvaR0qKGdbrLN1"
    RECAPTCHA_PRIVATE_KEY = "6Lc7ebAZAAAAAPmCqULtI1BscCtftz96M2QYNSD2"


class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:123456@127.0.0.1:3306/qianblog'
    
    # Celery <--> RabbitMQ connection
    CELERY_RESULT_BACKEND = "amqp://guest:guest@10.0.0.8:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@10.0.0.8:5672//"
    
    #### Flask-Cache's config
    CACHE_TYPE = 'simple'


