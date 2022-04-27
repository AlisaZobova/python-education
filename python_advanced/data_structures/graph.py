"""Graph implementation"""

#  pylint: disable=C0103

from graph_node import Node
from linked_list import LinkedList


class Graph:
    """Graph class"""
    def __init__(self):
        self.vertices = LinkedList()
        self.edges = LinkedList()
        self.length = 0
        self.num = 0

    def insert(self, neighbours=None):
        """Add new node"""
        node = Node(self.num)
        self.vertices.append(node)
        if neighbours:
            self.add_neighbours(neighbours, node)
            self.add_edges(node)
        self.length += 1
        self.num += 1

    def add_neighbours(self, neighbours, node):
        """Add node neighbours"""
        for i in range(len(neighbours)):
            for j in range(len(self.vertices)):
                if self.vertices[j].value == neighbours[i]:
                    node.neighbours.append(self.vertices[j])

    def add_edges(self, node):
        """Add edges with node"""
        for k in range(len(node.neighbours)):
            edge = LinkedList()
            edge.append(node)
            edge.append(node.neighbours[k])
            self.edges.append(edge)

    def lookup(self, value):
        """Search node by value"""
        for node in self.bfs():
            if node.value == value:
                return node

        return "No node with such value!"

    def delete(self, del_node):
        """Delete node by link"""
        for node in self.bfs():
            if node == del_node:
                ind = self.vertices.lookup(node)
                self.vertices.delete(ind)
                self.length -= 1
                self.delete_edges_neighbours(node)
                break

        else:
            print("No such node!")

    def delete_edges_neighbours(self, node):
        """Delete node neighbours and edges"""
        j = 0
        while j < len(self.edges):
            if self.edges[j][0] == node or self.edges[j][1] == node:
                self.edges.delete(j)
                j -= 1
            j += 1

        for p in range(len(self.vertices)):
            for i in self.vertices[p].neighbours:
                if i.value == node:
                    self.vertices[p].neighbours.delete(self.vertices[p].neighbours.lookup(i.value))

    def bfs(self):
        """
        Implements a breadth-first search algorithm that takes
        into account the possibility of having no neighbors
        """
        visited = LinkedList()
        find_queue = LinkedList()
        index = 0
        visited.append(self.vertices[index])
        find_queue.append(self.vertices[index])

        while not find_queue.is_empty():
            node = find_queue[0]
            find_queue.delete(0)

            yield node

            for k in range(len(node.neighbours)):
                if node.neighbours[k] not in visited:
                    visited.append(node.neighbours[k])
                    find_queue.append(node.neighbours[k])

            if find_queue.is_empty() and index < len(self.vertices) - 1:
                index += 1
                visited.append(self.vertices[index])
                find_queue.append(self.vertices[index])


MY_GRAPH = Graph()
MY_GRAPH.insert(None)
ex = LinkedList()
ex.append(0)
MY_GRAPH.insert(ex)
ex1 = LinkedList()
ex1.append(0)
ex1.append(1)
MY_GRAPH.insert(ex1)
ex2 = LinkedList()
ex2.append(1)
ex2.append(2)
MY_GRAPH.insert(ex2)
print("Graph vertices and their neighbours:")
for d in MY_GRAPH.vertices:
    print(d.value.value, ": ", end="", sep='')
    for t in range(len(d.value.neighbours)):
        print(d.value.neighbours[t].value, end=' ')
    print()
print("Graph edges:")
for d in MY_GRAPH.edges:
    print(d.value[0].value, '-', d.value[1].value)
print("Lookup 2:")
print(MY_GRAPH.lookup(2))
my_node = MY_GRAPH.vertices[2]
MY_GRAPH.delete(my_node)
print("Graph vertices and their neighbours after delete 2:")
for d in MY_GRAPH.vertices:
    print(d.value.value, ": ", end="", sep='')
    for t in range(len(d.value.neighbours)):
        print(d.value.neighbours[t].value, end=' ')
    print()
print("Graph edges after delete 2:")
for d in MY_GRAPH.edges:
    print(d.value[0].value, '-', d.value[1].value)
print("Lookup 2:")
print(MY_GRAPH.lookup(2))
