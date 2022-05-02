"""Recursive factorial implementation"""


def recursive_factorial(num):
    """Recursive factorial"""
    if num in (0, 1):
        return 1
    return num*recursive_factorial(num-1)
