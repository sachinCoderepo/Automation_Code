import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        FileHandler = logging.FileHandler("logfile.log")
        formet = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        FileHandler.setFormatter(formet)
        logger.addHandler(FileHandler)

        logger.setLevel(logging.DEBUG)
        return logger