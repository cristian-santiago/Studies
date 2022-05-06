
import logging
logger = logging.getLogger(__name__)


'''

logger.propagate = True
logger.debug("This is a debug  msg.")
logger.info("This is an info msg.")
logger.error("This is an error msg.")
logger.warning("This is a warning msg.")
logger.critical("This is a critical msg.")

'''

# Creating handlers

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log_file.log')

#Configure level and formatter and add it to handlers

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

#add handlers to the logger

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

class InfoFilter(logging.Filter):
    
    def filter(self, record):
        return record.levelno == logging.INFO

stream_handler.addFilter(InfoFilter())
logger.addHandler(stream_handler)

logger.warning('Warning msg')
logger.error('Error msg')
logger.info('Info msg')



