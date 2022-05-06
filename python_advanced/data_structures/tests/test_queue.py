"""Tests fot Queue class"""

import pytest
from python_advanced.data_structures.queue import Queue


@pytest.fixture(name="queue")
def fixture_queue():
    """Create Queue object"""
    return Queue()


@pytest.mark.parametrize("value", [1, 2, 3, 4, 5])
def test_enqueue(queue, value):
    """Check addition an element to the end of the queue"""
    queue.enqueue(value)
    assert queue.length == 1 and queue.peek() == value


def test_dequeue(queue):
    """Check removing an element from the front of the queue and its return"""
    queue.enqueue("v")
    queue.enqueue("a")
    assert queue.dequeue() == "v"


def test_dequeue_value_error(queue):
    """Checks for an error if the queue is empty"""
    with pytest.raises(ValueError):
        assert queue.dequeue()


def test_peek(queue):
    """Check getting the value of the element at the head of the queue"""
    queue.enqueue("v")
    queue.enqueue("a")
    assert queue.peek() == "v"


def test_peek_value_error(queue):
    """Checks for an error if the queue is empty"""
    with pytest.raises(ValueError):
        assert queue.peek()
