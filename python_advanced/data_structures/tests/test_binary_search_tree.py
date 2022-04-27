"""Tests for binary search tree class"""

import pytest
from python_advanced.data_structures.binary_search_tree import BinarySearchTree
from python_advanced.data_structures.binary_tree_node import Node


@pytest.fixture(name="bst")
def fixture_bst():
    """Create Binary search tree object"""
    return BinarySearchTree()


@pytest.fixture(name="root_bst")
def fixture_bst_with_root():
    """Create Binary search tree object with root"""
    return BinarySearchTree(Node(10))


@pytest.mark.parametrize("node_value, expected", [(Node(10), 10),
                                                  (Node(5), 5),
                                                  (Node(3), 3),
                                                  (Node(15), 15)])
def test_insert_bst(bst, node_value, expected):
    """Test add new element"""
    bst.insert(node_value)
    assert bst.root.value.value == expected


@pytest.mark.parametrize("node, value", [(Node(5), 5),
                                         (Node(3), 3),
                                         (Node(7), 7)])
def test_find_node_place_left(root_bst, node, value):
    """Test add new element to the right branch"""
    root_bst.insert(8)
    root_bst.find_node_place(node, value)
    assert root_bst.root.left.left.value == value


@pytest.mark.parametrize("node, value", [(Node(15), 15),
                                         (Node(13), 13),
                                         (Node(17), 17)])
def test_find_node_place_right(root_bst, node, value):
    """Test add new element to the left branch"""
    root_bst.insert(12)
    root_bst.find_node_place(node, value)
    assert root_bst.root.right.right.value == value


@pytest.mark.parametrize("node", [Node(15), Node(13), Node(17)])
def test_right_insert(root_bst, node):
    """Check correctness returned value of the right_insert method"""
    root_bst.insert(11)
    assert root_bst.right_insert(root_bst.root, node) == root_bst.root.right


@pytest.mark.parametrize("node", [Node(5), Node(3), Node(7)])
def test_left_insert(root_bst, node):
    """Check correctness returned value of the left_insert method"""
    root_bst.insert(9)
    assert root_bst.left_insert(root_bst.root, node) == root_bst.root.left


def test_lookup(root_bst):
    """Check lookup root node"""
    assert root_bst.lookup(10) == root_bst.root


def test_lookup_right(root_bst):
    """Check lookup root right node"""
    root_bst.insert(12)
    assert root_bst.lookup(12) == root_bst.root.right


def test_lookup_left(root_bst):
    """Check lookup root left node"""
    root_bst.insert(9)
    assert root_bst.lookup(9) == root_bst.root.left


def test_delete(root_bst):
    """Check delete root node"""
    root_bst.delete(10)
    assert root_bst.root is None


def test_not_left_or_right_left(root_bst):
    """Check delete root left node"""
    root_bst.insert(9)
    root_bst.delete(9)
    assert root_bst.root.left is None


def test_not_left_or_right_right(root_bst):
    """Check delete root right node"""
    root_bst.insert(15)
    root_bst.delete(15)
    assert root_bst.root.right is None


def test_node_offset(root_bst):
    """Check correctness of offset during removal"""
    root_bst.insert(15)
    root_bst.insert(8)
    root_bst.insert(7)
    root_bst.insert(9)
    root_bst.insert(5)
    root_bst.insert(6)
    root_bst.insert(19)
    root_bst.insert(17)
    root_bst.insert(18)
    root_bst.insert(21)
    root_bst.delete(7)
    root_bst.delete(19)
    assert root_bst.root.left.left.value == 5 \
           and root_bst.root.right.right.value == 18 \
           and root_bst.root.right.right.left.value == 17
