"""Tests for recursive factorial algorithm"""

import sys
import math
from random import randint
import pytest
from python_advanced.algorithms.recursive_factorial import recursive_factorial

sys.setrecursionlimit(2000)


@pytest.mark.parametrize("num", (randint(0, 1000) for _ in range(100)))
def test_recursive_factorial(num):
    """Compares the result of my factorial function and the math module function"""
    assert recursive_factorial(num) == math.factorial(num)
