import logging

FORMAT = '%(asctime)s %(levelname)s [%(name)s]: %(message)s    (%(filename)s:%(lineno)d)'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('httpserver')
logger.setLevel(level=logging.INFO)

logger.warning('Protocol problem: %s', 'connection refused')
logger.info('Protocol info: %s', 'Using HTTPs')
