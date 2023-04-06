import secrets


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_urlsafe(32)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
