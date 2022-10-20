import logging


def test_loggingDemo():

    logger = logging.getLogger(__name__)

    FileHandler = logging.FileHandler("logfile.log")
    formet = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    FileHandler.setFormatter(formet)
    logger.addHandler(FileHandler)

    logger.setLevel(logging.DEBUG)

    

    logger.debug("print debug statement")
    logger.info("print the information")
    logger.warning("print the warning msz")
    logger.error("print the error message")
    logger.critical("print remain information")
