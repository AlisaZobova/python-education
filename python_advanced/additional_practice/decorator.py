"""Decorator for logging functions executed time"""

from datetime import datetime
from loggers import logger


def time_logger(func):
    """Decorator"""
    def func_time(*args, **kwargs):
        """Get main function`s result"""
        time_before = datetime.now()
        func_result = func(*args, **kwargs)
        logger.info("%s executed time: %s.", func.__name__, str(datetime.now() - time_before))
        return func_result

    return func_time


@time_logger
def congratulation(name):
    """Congratulate with HB"""
    print(f"Happy Birthday, {name}!")


congratulation("Pavel")
