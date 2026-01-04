# backend/root/root.py
import os

from app.logger import logging
logging.info('log successfull')
def root_name():
    return os.getcwd()
 