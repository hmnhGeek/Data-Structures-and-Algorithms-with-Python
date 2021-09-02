class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def enqueue(self, data):
        node = Node(data)

        # add nodes to the end, i.e., last
        
        if self.is_empty():
            self.last = node
            self.first = self.last

        else:
            self.last.next = node
            self.last = node

        self.len += 1

    def dequeue(self):
        if not self.is_empty():
            first_that_came = self.first
            self.first = self.first.next
            data = first_that_came.data

            del first_that_came
            self.len -= 1
            return data
        else:
            return "Queue empty"

    def peek(self):
        if not self.is_empty():
            return self.first.data

    def info(self):
        if not self.is_empty():
            return {'first': self.first.data, 'last': self.last.data, 'length': self.len}
        else:
            return {'first': None, 'last': None, 'length': 0}
    
