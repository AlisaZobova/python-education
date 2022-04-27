"""Graph node"""
from linked_list import LinkedList

#  pylint: disable=R0903


class Node:
    """Graph node"""
    def __init__(self, value):
        self.value = value
        self.neighbours = LinkedList()
