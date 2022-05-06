"""Tests fot Linked List class"""

import pytest
from python_advanced.data_structures.linked_list import LinkedList


@pytest.fixture(name="link_list")
def fixture_link_list():
    """Create LinkedList object"""
    return LinkedList()


@pytest.mark.parametrize("value", [1, 2, 3, "cold", "water"])
def test_prepend(link_list, value):
    """Check addition an element to the beginning of the list"""
    link_list.prepend("lemon")
    link_list.prepend("nose")
    length_before = link_list.length
    link_list.prepend(value)
    assert link_list[0] == value and link_list.length - length_before == 1


@pytest.mark.parametrize("value", [1, 2, 3, "cold", "water"])
def test_append(link_list, value):
    """Check addition an element to the end of the list"""
    link_list.append("lemon")
    link_list.append("nose")
    length_before = link_list.length
    link_list.append(value)
    assert link_list[-1] == value and link_list.length - length_before == 1


def test_lookup(link_list):
    """Check searching index of element"""
    link_list.append("lemon")
    link_list.append("nose")
    assert link_list.lookup("lemon") == 0 and link_list.lookup("nose") == 1


@pytest.mark.parametrize("value, index", [(1, 2), (2, 3), ("cold", 0), ("water", 1)])
def test_insert(link_list, value, index):
    """Check inserting function"""
    link_list.append("lemon")
    link_list.append("nose")
    link_list.append("form")
    link_list.append("rose")
    length_before = link_list.length
    link_list.insert(index, value)
    assert link_list[index] == value and link_list.length - length_before == 1


def test_delete(link_list):
    """Check did the list shrink after deletion"""
    link_list.append("lemon")
    link_list.append("nose")
    link_list.append("form")
    link_list.append("rose")
    length_before = link_list.length
    link_list.delete(1)
    assert length_before - link_list.length == 1


def test_delete_error(link_list):
    """Checks for an error when trying to remove a non-existent element"""
    link_list.append("lemon")
    link_list.append("nose")
    link_list.append("form")
    link_list.append("rose")
    link_list.delete(1)
    with pytest.raises(ValueError):
        assert link_list.lookup("nose")


def test_is_empty_true(link_list):
    """Checks if the function returns true if the list is empty"""
    assert link_list.is_empty() is True


def test_is_empty_false(link_list):
    """Checks if the function returns false if the list is not empty"""
    link_list.append("lemon")
    assert link_list.is_empty() is False


def test_get_item(link_list):
    """Checks whether an element can be retrieved by index"""
    link_list.append("lemon")
    assert link_list[0] == link_list[-1] == "lemon"


def test_set_item(link_list):
    """Checks if an element can be set by index"""
    link_list.append("rose")
    link_list[0] = "lemon"
    assert link_list[0] == "lemon"


def test_iter(link_list):
    """Check __iter__ function"""
    link_list.append("lemon")
    link_list.append("nose")
    link_list.append("form")
    link_list.append("rose")
    for i in range(link_list.length):
        assert link_list[i] == link_list[i]


def test_len(link_list):
    link_list.append("lemon")
    link_list.append("nose")
    link_list.append("form")
    link_list.append("rose")
    link_list.delete(1)
    assert len(link_list) == 3