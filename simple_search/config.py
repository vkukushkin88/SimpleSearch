
class Config(object):
    DEBUG = False

    API_VERSION = 'v1'

    SERVER_HOST = None
    API_PORT = 8080

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/database.db'

    LOG_LEVEL = DEBUG
    LOG_3D_PARTY_LEVEL = 'CRITICAL'
    LOG_DEFAULT_SERVER = 'ERROR'
    LOG_FORMAT = ('%(name)s %(levelname)-8s %(asctime)s '
                  '[%(filename)s,%(lineno)d] -- %(message)s')
    LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'

    DATA_FILE_PATH = 'data/storage.st'
