"""Linked List implementation"""

from node import Node


class LinkedList:
    """Linked List class"""
    def __init__(self):
        self.head_val = None
        self.length = 0

    def prepend(self, value):
        """Add an element to the beginning of the list"""
        new_node = Node(value)
        new_node.next_node = self.head_val
        self.head_val = new_node
        self.length += 1

    def append(self, value):
        """Add an element to the end of the list"""
        new_node = Node(value)
        if self.head_val is None:
            self.head_val = new_node
        else:
            node = self.head_val
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
        self.length += 1

    def lookup(self, value):
        """Search element by value"""
        index = 0
        node = self.head_val

        while node:

            if node.value == value:
                return index

            if index == self.length - 1:
                raise ValueError("There is no such value!")

            node = node.next_node
            index += 1

    def insert(self, node_index, value):
        """Insert element by index"""
        if node_index < 0:
            node_index = self.length + node_index

        if node_index >= self.length:
            raise IndexError("There is no such index!")

        if node_index == 0:
            self.prepend(value)

        else:
            count = 0
            node = self.head_val
            while node:
                if count == node_index - 1:
                    new_node = Node(value, node.next_node)
                    node.next_node = new_node
                    break
                node = node.next_node
                count += 1

            self.length += 1

    def delete(self, node_index):
        """Delete element by index"""
        if node_index < 0:
            node_index = self.length + node_index

        if node_index >= self.length:
            raise IndexError("There is no such index!")

        if node_index == 0:
            self.head_val = self.head_val.next_node
            self.length -= 1

        else:
            count = 0
            node = self.head_val
            while node:
                if count == node_index - 1:
                    node.next_node = node.next_node.next_node
                    break

                node = node.next_node
                count += 1

            self.length -= 1

    def is_empty(self):
        """Checks if the list is empty"""
        if self.length == 0:
            return True
        return False

    def __getitem__(self, index):
        """Overridden method __getitem__ to get element by index"""
        if index < 0:
            index = self.length + index

        if index > self.length - 1:
            return "Index out of range!"

        current_val = self.head_val
        for _ in range(index):
            current_val = current_val.next_node
        return current_val.value

    def __setitem__(self, index, value):
        """Overridden method __setitem__ to set element by index"""
        if index < 0:
            index = self.length + index

        if index > self.length - 1:
            print("Index out of range!")

        current_val = self.head_val
        for _ in range(index):
            current_val = current_val.next_node
        current_val.value = value

    def __iter__(self):
        """Class iterator"""
        node = self.head_val
        while node:
            yield node
            node = node.next_node

    def __len__(self):
        """Method to return length"""
        return self.length

    def list_print(self):
        """Print all elements"""
        print_val = self.head_val
        while print_val:
            print(print_val.value)
            print_val = print_val.next_node


if __name__ == "__main__":
    MY_LIST = LinkedList()
    print("Empty list:")
    MY_LIST.list_print()
    print("Append 1, 2, 3, 4, 5:")
    MY_LIST.append(1)
    MY_LIST.append(2)
    MY_LIST.append(3)
    MY_LIST.append(4)
    MY_LIST.append(5)
    print("Head:")
    print(MY_LIST.head_val.value)
    print("List:")
    MY_LIST.list_print()
    print("Prepend 0:")
    MY_LIST.prepend(0)
    print("Head:")
    print(MY_LIST.head_val.value)
    print("List:")
    MY_LIST.list_print()
    print("Insert 6 per index 2:")
    MY_LIST.insert(2, 6)
    print("Head:")
    print(MY_LIST.head_val.value)
    print("List:")
    MY_LIST.list_print()
    print("Lookup 5:")
    print(MY_LIST.lookup(5))
    print("Delete value per index 0")
    MY_LIST.delete(0)
    print("Head:")
    print(MY_LIST.head_val.value)
    print("List:")
    MY_LIST.list_print()
    print("List[-2]:")
    print(MY_LIST[-2])
    print("List by for:")
    for i in MY_LIST:
        print(i.value)
