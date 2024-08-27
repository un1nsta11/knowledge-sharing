import os
import logging
from logging import config
import traceback

logging.config.fileConfig(os.path.join(os.getcwd(), 'logconf.ini'))
logging = logging.getLogger('zeus')


def new_function():
    logging.info("This is information message")
    with open("NoFile", "r") as data:
        data.readlines()
    logging.warning("Should never goes here! File was found while should not be!")


if __name__ == '__main__':
    logging.debug("Debugging message")
    logging.info("Function executed. No errors, was found item in index 3")
    logging.warning("First time item was not found, but second")
    logging.error("Error")
    logging.fatal("Application work completed")
    new_function()
    logging.info("New function to continue application")


