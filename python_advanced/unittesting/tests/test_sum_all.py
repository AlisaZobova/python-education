"""Tests for sum_all method"""

import pytest
from python_advanced.unittesting.to_test import sum_all


@pytest.mark.parametrize("numbers, expected", [([1, 5, 8, 9], 23),
                                               ([2, 5, 9, 9], 25),
                                               ([2, 5, 4, 9], 20)])
def test_sum_all(numbers, expected):
    """Check the correctness of the calculation"""
    assert sum_all(*numbers) == expected


@pytest.mark.parametrize("elems, exception", [(["f", "b", "c"], TypeError),
                                              (([2, 5], [9, 9]), TypeError)])
def test_sum_all_type_error(elems, exception):
    """Check the occurrence of TypeError"""
    with pytest.raises(exception):
        assert sum_all(elems)
