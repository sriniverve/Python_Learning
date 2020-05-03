'''
This is to demonstrate the usage of logging
'''

import logging

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

stream_h.setLevel(logging.DEBUG)
file_h.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')





