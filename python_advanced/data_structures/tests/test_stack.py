"""Tests fot Stack class"""

import pytest
from python_advanced.data_structures.stack import Stack


@pytest.fixture(name="stack")
def fixture_stack():
    """Create Stack object"""
    return Stack()


@pytest.mark.parametrize("value", [1, 2, 3, 4, 5])
def test_push(stack, value):
    """Check addition an element to the stack"""
    stack.push(value)
    assert stack.length == 1 and stack.peek() == value


def test_pop(stack):
    """Check removing an element from the stack and its return"""
    stack.push("v")
    stack.push("a")
    assert stack.pop() == "a"


def test_pop_value_error(stack):
    """Checks for an error if the stack is empty"""
    with pytest.raises(ValueError):
        assert stack.pop()


def test_peek(stack):
    """Check getting the value of the element at the head of the stack"""
    stack.push("v")
    stack.push("a")
    assert stack.peek() == "a"


def test_peek_value_error(stack):
    """Checks for an error if the stack is empty"""
    with pytest.raises(ValueError):
        assert stack.peek()
