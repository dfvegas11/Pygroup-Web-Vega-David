class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///shop.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATION = False
    WTF_CSRF_ENABLED = False

class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

class TestingConfig(Config):
    TESTING = True