import datetime
import logging
import os


def log():
    logger = logging.getLogger('HomeWork')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s：%(name)s::%(filename)s::%(funcName)s -- %(levelname)s - %(message)s')
    # sh = logging.StreamHandler()
    # sh.setLevel(logging.DEBUG)
    # sh.setFormatter(formatter)
    # logger.addHandler(sh)

    date = str(datetime.date.today()) + "-" + 'test_log.log'
    path = os.path.join(os.path.abspath(os.path.pardir), 'log', date)
    fh = logging.FileHandler(path, encoding='utf8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    if len(logger.handlers) == 1:
        return logger
    del logger.handlers[0]
    return logger
