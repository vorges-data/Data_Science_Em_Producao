import os
import logging
from logging.config import fileConfig

BASE_DIR = os.path.join(os.path.abspath('.'))
LOG_DIR = os.path.join( BASE_DIR, 'logger' )

def log_config():
    fileConfig(os.path.join(LOG_DIR, 'logging_config.ini'))
    logger = logging.getLogger('root')
    
    return logger
    