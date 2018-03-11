import logging

#filehandler = logging.basicConfig(filename='example123.log',level=logging.WARNING, filemode='w')
logger = logging.getLogger('MY_FIRST_LOGGER')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler = logging.FileHandler('exampleHandler.log', mode='w')
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
# create formatter
