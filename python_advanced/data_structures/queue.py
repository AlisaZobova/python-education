"""Queue implementation"""

from node import Node


class Queue:
    """Queue class"""
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        """Add an element to the end of the queue"""
        if self.last is None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next_node = Node(value)
            self.last = self.last.next_node
        self.length += 1

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.head:
            value = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            return value
        raise ValueError("No items in queue!")

    def peek(self):
        """Get the value of the element at the head of the queue"""
        if self.head:
            value = self.head.value
            return value
        raise ValueError("No items in queue!")

    def queue_print(self):
        """Print queue"""
        print_val = self.head
        num = 1
        while print_val:
            print(num, "-", print_val.value)
            print_val = print_val.next_node
            num += 1


MY_QUEUE = Queue()
print("Add Vasya, Katya, Vova to the queue:")
MY_QUEUE.enqueue("Vasya")
MY_QUEUE.enqueue("Katya")
MY_QUEUE.enqueue("Vova")
MY_QUEUE.queue_print()
print("First dequeue:")
MY_QUEUE.dequeue()
MY_QUEUE.queue_print()
print("Second dequeue:")
MY_QUEUE.dequeue()
MY_QUEUE.queue_print()
print("Peek:")
print(MY_QUEUE.peek())
