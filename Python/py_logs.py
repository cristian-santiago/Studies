# The logging mudule is a built-in module so you can add logging to an application

import logging

#Basic log levels

'''
logging.debug("This is a debug msg.")
logging.info("This is an info msg")
logging.warning('This is a warning msg.')
logging.error("This is an error msg.")
logging.critical('This is a critical msg.')

'''
# Configuration

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt= '%m/%d/%Y %H:%M:%S', filename='my_log.log')
#logging.debug('Debug message')

# Logging in modules: This msg below comes from a module on log_help.py file)
import log_help

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt= '%m/%d/%Y %H:%M:%S', filename='my_log.log')
# logging.info('Info message') won't be necessary

# Propagation, if settle as False, the log events won't be passed to the handlers
#logger.propagate = False

# LogHandlers

