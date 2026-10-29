# LinkedStack Implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek.")
        return self.top.value

    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return " -> ".join(map(str, elements)) + " (Top)" if elements else "Empty"
