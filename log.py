import logging

class Log:
    def __init__(self, filename:str, logname:str):
        logger = logging.getLogger(logname)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.FileHandler(filename, encoding= 'utf-8')
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        self.logger = logger

    def debug(self, s:str):
        self.logger.debug(s)
    def info(self, s:str):
        self.logger.info(s)
    def warning(self, s:str):
        self.logger.warning(s)
    def error(self, s:str):
        self.logger.error(s)
