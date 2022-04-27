"""Stack implementation"""

from node import Node


class Stack:
    """Stack class"""
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def push(self, value):
        """Add element to stack"""
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        """Remove the last element and return its value"""
        if self.head:
            value = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            return value
        raise ValueError("No items in stack!")

    def peek(self):
        """Get the value of the top element of the stack"""
        if self.head:
            value = self.head.value
            return value
        raise ValueError("No items in stack!")

    def stack_print(self):
        """Print stack"""
        print_val = self.head
        num = self.length
        while print_val:
            print(num, "-", print_val.value)
            print_val = print_val.next_node
            num -= 1


MY_STACK = Stack()
print("Add Vasya, Katya, Vova to the stack:")
MY_STACK.push("Vasya")
MY_STACK.push("Katya")
MY_STACK.push("Vova")
MY_STACK.stack_print()
print("First pop:")
print(MY_STACK.pop())
print("Stack:")
MY_STACK.stack_print()
print("Second pop:")
print(MY_STACK.pop())
print("Stack:")
MY_STACK.stack_print()
print("Peek:")
print(MY_STACK.peek())
