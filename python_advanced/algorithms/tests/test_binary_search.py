"""Tests for binary search algorithm"""


from random import randint, choice
import pytest
from python_advanced.algorithms.binary_search import binary_search


@pytest.mark.parametrize("unsorted_list",
                         (list(set(randint(-70, 70) for _ in range(100))) for _ in range(100)))
def test_binary_search(unsorted_list):
    """Check correctness of binary search algorithm"""
    num = choice(unsorted_list)
    unsorted_list.sort()
    print(unsorted_list)
    assert binary_search(unsorted_list, num) == unsorted_list.index(num)
