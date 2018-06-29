import logging
from flask import Blueprint


logger = logging.getLogger(__name__)
main = Blueprint('about', __name__)


@main.route('/')
def index():
    logger.warning('Welcome to About Page')
    return 'Welcome to About Page'

