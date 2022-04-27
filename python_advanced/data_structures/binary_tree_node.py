"""Binary search tree node"""

#  pylint: disable=R0903


class Node:
    """Binary search tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
