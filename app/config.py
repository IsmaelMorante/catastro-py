import os


class Config(object):
    DEBUG = False
    SECRET_KEY = "\xc6\xebR\xf1\xf3\xcf\x08)\x89\xdeX\xcd\xc6\xa1a\xaa\x05\xeb6\xb5\x996\xb6"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin1234@localhost:5432/catastro'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
