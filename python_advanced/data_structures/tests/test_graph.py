"""Tests for Graph class"""

import pytest
from python_advanced.data_structures.graph import Graph
from python_advanced.data_structures.linked_list import LinkedList


@pytest.fixture(name="graph")
def fixture_graph():
    """Create Graph object"""
    return Graph()


def test_insert(graph):
    """Test insert method"""
    graph.insert()
    assert graph.vertices[0].value == 0


def test_add_neighbours_edges(graph):
    """Check the addition of the neighbors and the formation of edges"""
    graph.insert()
    ex = LinkedList()
    ex.append(0)
    graph.insert(ex)
    assert graph.vertices.length == 2 \
           and graph.vertices[1].neighbours.length == 1 \
           and graph.edges.length == 1


def test_lookup(graph):
    """Check lookup function"""
    graph.insert()
    ex = LinkedList()
    ex.append(0)
    graph.insert(ex)
    assert graph.lookup(0) == graph.vertices[0] and graph.lookup(1) == graph.vertices[1]


def test_delete(graph):
    """
    Check the removal of nodes, edges with them and the removal
    of these nodes from the list of neighbours of other nodes
    """
    graph.insert()
    ex = LinkedList()
    ex.append(0)
    graph.insert(ex)
    node = graph.vertices[0]
    graph.delete(node)
    assert graph.vertices[0].neighbours.length == 0 \
           and graph.vertices.length == 1 \
           and graph.edges.length == 0
