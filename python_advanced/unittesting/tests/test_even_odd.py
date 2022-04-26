"""Tests for even_odd method"""

import pytest
from python_advanced.unittesting.to_test import even_odd


@pytest.mark.parametrize("num, expected", [(1, "odd"),
                                           (2, "even"),
                                           (3, "odd"),
                                           (4, "even")])
def test_even_odd_even(num, expected):
    """Check returned value"""
    assert even_odd(num) == expected


def test_even_odd_even_type_error():
    """Check the occurrence of TypeError"""
    with pytest.raises(TypeError):
        assert even_odd("f")
