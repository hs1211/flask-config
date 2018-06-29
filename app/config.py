import os
import logging
import logging.handlers

import sys

config = {
    'local': 'app.config.LocalConfig',
    'dev': 'app.config.DevelopmentConfig',
    'prod': 'app.config.ProductionConfig'
}


class BaseConfig(object):
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/test.log'
    ACCESS_LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    ACCESS_LOGGING_LOCATION = 'logs/access.log'
    LOGGING_LEVEL = logging.DEBUG


class LocalConfig(BaseConfig):
    CONFIG_LOCATION = 'config.cfg'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/test.log'
    ACCESS_LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    ACCESS_LOGGING_LOCATION = 'logs/access.log'
    LOGGING_LEVEL = logging.DEBUG


class DevelopmentConfig(BaseConfig):
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'test.log'
    ACCESS_LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    ACCESS_LOGGING_LOCATION = 'logs/access.log'
    LOGGING_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'test.log'
    ACCESS_LOGGING_FORMAT = '%(asctime)s %(levelname)s %(message)s'
    ACCESS_LOGGING_LOCATION = 'logs/access.log'
    LOGGING_LEVEL = logging.DEBUG


def configure_app(app):
    stage = os.getenv('FLASK_CONFIG', 'local')
    app.config.from_object(config[stage])
    app.config.from_pyfile(os.path.join(root_path(),app.config['CONFIG_LOCATION']))

    # Configure logging
    mkdir(app.config['LOGGING_LOCATION'])
    handler = logging.handlers.RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=10000)
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    time_handler= logging.handlers.TimedRotatingFileHandler(app.config['ACCESS_LOGGING_LOCATION'], interval=30, backupCount=10)
    time_handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['ACCESS_LOGGING_FORMAT'])
    time_handler.setFormatter(formatter)
    logging.getLogger('uwsgi').addHandler(time_handler);


def mkdir(log_path):
    directory = os.path.dirname(log_path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)


def root_path():
    # Infer the root path from the run file in the project root (e.g. manage.py)
    fn = getattr(sys.modules['__main__'], '__file__')
    return os.path.abspath(os.path.dirname(fn))
