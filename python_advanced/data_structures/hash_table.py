"""Hash Table implementation"""

from hash_table_node import Node
from linked_list import LinkedList

#  pylint: disable=E1101


class HashTable:
    """Hash Table class"""
    def __init__(self):
        self.capacity = 30
        self.length = 0
        self.table = LinkedList()
        for _ in range(30):
            self.table.append(None)

    @staticmethod
    def hash(key):
        """Return key`s hash"""
        hash_sum = 0
        for i in key:
            hash_sum += ord(i)
        return hash_sum % 30

    def insert(self, key, value):
        """
        Add new key and value in table, if the cell is not
        empty - creates a linked list writes to it the
        key-value pair that was in the cell and the new pair
        """
        self.length += 1
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        elif not isinstance(self.table[index], LinkedList):
            self.table[index] = LinkedList()
            self.table[index].append(node)
            self.table[index].append(Node(key, value))
        else:
            self.table[index].append(Node(key, value))

    def lookup(self, key):
        """Search value by key"""
        index = self.hash(key)
        node = self.table[index]
        if not isinstance(node, LinkedList):
            return node.value
        for i in range(len(node)):
            if node[i].key == key:
                return node[i].value
        return None

    def delete(self, key):
        """Delete key-value pair by key"""
        index = self.hash(key)
        node = self.table[index]
        if not isinstance(node, LinkedList):
            self.table[index] = None
            self.length -= 1
            return

        for i in range(node.length):
            if node[i].key == key:
                self.table[index].delete(i)
                break

        else:
            print("No such key!")


MY_HASH_TABLE = HashTable()
MY_HASH_TABLE.insert("lies", "ложь")
MY_HASH_TABLE.insert("foes", "враги")
MY_HASH_TABLE.insert("Exxx", "smth")
print('Add "lies": "ложь", "foes": "враги", "Exxx": "smth":')
print("Hash table [9]:")
for k in range(len(MY_HASH_TABLE.table[9])):
    print(MY_HASH_TABLE.table[9][k].key, '-', MY_HASH_TABLE.table[9][k].value)
print("Lookup lies:")
print(MY_HASH_TABLE.lookup("lies"))
print("Lookup foes:")
print(MY_HASH_TABLE.lookup("foes"))
print("Delete lies:")
MY_HASH_TABLE.delete("lies")
print("Hash table [9] now:")
for k in range(len(MY_HASH_TABLE.table[9])):
    print(MY_HASH_TABLE.table[9][k].key, '-', MY_HASH_TABLE.table[9][k].value)
print("Lookup lies:")
print(MY_HASH_TABLE.lookup("lies"))
print("Delete lies:")
MY_HASH_TABLE.delete("lies")
