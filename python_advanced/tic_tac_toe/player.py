"""Class player"""
from loggers import logger

# pylint: disable=R0903


class Player:
    """Class player"""
    def __init__(self, name: str):
        self.name = name
        self.num = None
        self.victories = 0

    def print_victories(self):
        """Method for printing victories amount"""
        logger.critical("%s: %s victories.", self.name, self.victories)
