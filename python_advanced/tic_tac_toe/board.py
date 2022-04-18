"""Class board"""

# pylint: disable=R0903


class Board:
    """Class board"""
    def __init__(self):
        self.field = [[" "] * 3 for _ in range(3)]

    def clear(self):
        """Method for clearing a field"""
        self.field = [[" "] * 3 for _ in range(3)]
