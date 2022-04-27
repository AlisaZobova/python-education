"""Tests fot Hash Table class"""

import pytest
from python_advanced.data_structures.hash_table import HashTable


@pytest.fixture(name="hash_table")
def fixture_hash_table():
    """Create HashTable object"""
    return HashTable()


@pytest.mark.parametrize("string, expected", [("look", 17), ("book", 7), ("game", 20)])
def test_hash(hash_table, string, expected):
    """Check hash function"""
    assert hash_table.hash(string) == expected


@pytest.mark.parametrize("string, expected", [("look", 17), ("book", 7), ("game", 20)])
def test_insert_empty(hash_table, string, expected):
    """Check insert into empty cell"""
    hash_table.insert(string, string)
    assert hash_table.table[expected] is not None


def test_insert_list(hash_table):
    """
    Check insert into occupied cell: a linked list
    should be created with all nodes with this key
    """
    hash_table.insert("lies", "ложь")
    hash_table.insert("foes", "враги")
    hash_table.insert("Exxx", "smth")
    assert hash_table.table[9].length == 3


@pytest.mark.parametrize("string, value, expected", [("look", 1, 17),
                                                     ("book", 2, 7),
                                                     ("game", 3, 20)])
def test_lookup(hash_table, string, value, expected):
    """Check searching for a value in a cell that has only one node"""
    hash_table.insert(string, value)
    assert hash_table.lookup(string) == value


def test_lookup_list(hash_table):
    """Check searching for a value in a cell that has linked list with nodes"""
    hash_table.insert("lies", "ложь")
    hash_table.insert("foes", "враги")
    hash_table.insert("Exxx", "smth")
    assert hash_table.lookup("foes") == "враги"


@pytest.mark.parametrize("string, value, expected", [("look", 1, 17),
                                                     ("book", 2, 7),
                                                     ("game", 3, 20)])
def test_delete(hash_table, string, value, expected):
    """Check deleting for a value in a cell that has only one node"""
    hash_table.insert(string, value)
    hash_table.delete(string)
    assert hash_table.table[expected] is None


def test_delete_list(hash_table):
    """Check deleting for a value in a cell that has linked list with nodes"""
    hash_table.insert("lies", "ложь")
    hash_table.insert("foes", "враги")
    hash_table.insert("Exxx", "smth")
    hash_table.delete("foes")
    assert hash_table.lookup("foes") is None
