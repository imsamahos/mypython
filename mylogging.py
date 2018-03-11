import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
#formattedMsg = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.debug('%(asctime)s - %(name)s - %(levelname)s - This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')
