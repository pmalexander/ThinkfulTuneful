class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/tuneful-pa"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"

#creates testing environment for config
class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/tuneful-test-pa"
    DEBUG = True
    UPLOAD_FOLDER = "test-uploads"
