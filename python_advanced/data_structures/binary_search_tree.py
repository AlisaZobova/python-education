"""Binary Search Tree implementation"""
from binary_tree_node import Node


class BinarySearchTree:
    """Binary Search Tree class"""
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """Add new element"""
        node = Node(value)

        if self.root is None:
            self.root = node

        else:
            self.find_node_place(node, value)

    def find_node_place(self, node, value):
        """Find place for a new element"""
        find_node = self.root
        while find_node is not None:
            if find_node.value > value:
                find_node = self.left_insert(find_node, node)
            elif find_node is not None and find_node.value < value:
                find_node = self.right_insert(find_node, node)
            else:
                print("This value already exists!")

    @staticmethod
    def left_insert(find_node, node):
        """Inserts into the left branch"""
        if find_node.left is None:
            find_node.left = node
            return None
        find_node = find_node.left
        return find_node

    @staticmethod
    def right_insert(find_node, node):
        """Inserts into the right branch"""
        if find_node.right is None:
            find_node.right = node
            return None
        find_node = find_node.right
        return find_node

    def lookup(self, value):
        """Search element by value"""
        root = self.root
        while root is not None:

            if value > root.value:
                root = root.right

            elif value < root.value:
                root = root.left
            else:
                return root

    def delete(self, value):
        """Delete element by value"""
        curr = self.root
        prev = None

        while curr is not None and curr.value != value:
            prev = curr
            if curr.value < value:
                curr = curr.right
            else:
                curr = curr.left

        if curr is None:
            print("Key % d not found." % value)
            return

        if prev is None:
            self.root = None

        elif curr.left is None or curr.right is None:
            self.not_left_or_right(curr, prev)

        else:
            self.node_offset(curr)

    @staticmethod
    def not_left_or_right(curr, prev):
        """Calls while deleting a node if left or right branch is None"""
        if curr.left is None:
            new_curr = curr.right
        else:
            new_curr = curr.left

        if curr == prev.left:
            prev.left = new_curr
        else:
            prev.right = new_curr

    @staticmethod
    def node_offset(curr):
        """
        Moves nodes after deletion. If there is a node with a lower value on the left,
        it replaces the vacated space with it; if not, it pulls nodes from the right branch.
        """
        node = None
        temp = curr.left

        while temp.right is not None:
            node = temp
            temp = temp.right

        if node is not None:
            node.left = temp.right

        else:
            curr.right = temp.left

        curr.value = temp.value


MY_BINARY_SEARCH_TREE = BinarySearchTree()
print("Insert 15, 13, 17:")
MY_BINARY_SEARCH_TREE.insert(15)
MY_BINARY_SEARCH_TREE.insert(13)
MY_BINARY_SEARCH_TREE.insert(17)
print("Root value:")
print(MY_BINARY_SEARCH_TREE.root.value)
print("Root right value:")
print(MY_BINARY_SEARCH_TREE.root.right.value)
print("Root left value:")
print(MY_BINARY_SEARCH_TREE.root.left.value)
print("Insert 27, 37, 25:")
MY_BINARY_SEARCH_TREE.insert(27)
MY_BINARY_SEARCH_TREE.insert(37)
MY_BINARY_SEARCH_TREE.insert(25)
print("Root value:")
print(MY_BINARY_SEARCH_TREE.root.value)
print("Root right value:")
print(MY_BINARY_SEARCH_TREE.root.right.value)
print("Root right right value:")
print(MY_BINARY_SEARCH_TREE.root.right.right.value)
print("Root right right right value:")
print(MY_BINARY_SEARCH_TREE.root.right.right.right.value)
print("Root left value:")
print(MY_BINARY_SEARCH_TREE.root.left.value)
print('Lookup 27:')
print(MY_BINARY_SEARCH_TREE.lookup(27))
print('Delete 27:')
MY_BINARY_SEARCH_TREE.delete(27)
print("Root right right value:")
print(MY_BINARY_SEARCH_TREE.root.right.right.value)
print('Lookup 27:')
print(MY_BINARY_SEARCH_TREE.lookup(27))
print('Delete 17:')
MY_BINARY_SEARCH_TREE.delete(17)
print("Root right value:")
print(MY_BINARY_SEARCH_TREE.root.right.value)
print("Insert 11 and delete 13:")
MY_BINARY_SEARCH_TREE.insert(11)
MY_BINARY_SEARCH_TREE.delete(13)
print("Root left value:")
print(MY_BINARY_SEARCH_TREE.root.left.value)
MY_BINARY_SEARCH_TREE.delete(15)
print(MY_BINARY_SEARCH_TREE.lookup(15))
print(MY_BINARY_SEARCH_TREE.root)
