class SpecialStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.min = []
    
    def push(self, item):

        # O(n)
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            return "Stack is full"

    def pop(self):
        # O(1)
        item = self.stack[-1]
        del self.stack[-1]

        return item
    
    def isEmpty(self):
        # O(1)
        return len(self.stack) == 0

    def isFull(self):
        # O(1)
        return len(self.stack) == self.capacity

    def getMin(self):
        # O(n)
        MIN = 0

        for i in range(len(self.stack)):
            if self.stack[i] < self.stack[MIN]:
                MIN = i

        return self.stack[MIN]