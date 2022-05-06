"""Hash Table node"""

#  pylint: disable=R0903


class Node:
    """Hash Table node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
