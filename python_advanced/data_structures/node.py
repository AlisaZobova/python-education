"""Node for linked_list, queue, stack"""

#  pylint: disable=R0903


class Node:
    """Node for linked_list, queue, stack"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
