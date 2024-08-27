import logging
from logging import config
import os

logging.config.fileConfig(os.path.join(os.getcwd(), 'logconf.ini'))
logging = logging.getLogger('zeus')




