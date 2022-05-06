"""Tests for quick sort algorithm"""

from random import randint
import pytest
from python_advanced.algorithms.quick_sort import quick_sort


@pytest.mark.parametrize("unsorted_list",
                         ([randint(-70, 70) for _ in range(100)] for _ in range(100)))
def test_quick_sort(unsorted_list):
    """Compares the result of my quick sort function and the built-in function sort"""
    assert quick_sort(unsorted_list) == unsorted_list.sort()
