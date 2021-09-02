class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0

    def push(self, data):
        new_node = Node(data)
        
        if not self.len:
            self.top = new_node
            self.bottom = self.top

        else:
            top_node = self.top
            self.top = new_node
            new_node.next = top_node

        self.len += 1

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def pop(self):

        if self.len:
            topmost = self.top
            self.top = topmost.next

            topmost_value = topmost.data
            del topmost

            self.len -= 1

            return topmost_value

        else:
            return "Stack empty"

    def is_empty(self):
        return self.len == 0

    def info(self):
        if not self.is_empty():
            return {'top': self.top.data, 'bottom': self.bottom.data, 'length': self.len}
        else:
            return {'top': None, 'bottom': None, 'length': 0}
