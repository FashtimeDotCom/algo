# coding:utf-8

import logging
import logging.config

# logger
logger_file = "./conf/logger.ini"
logger_handler="rotate_file"
logging.config.fileConfig(logger_file)
logger = logging.getLogger(logger_handler)
