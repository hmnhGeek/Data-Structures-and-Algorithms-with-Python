class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        leng = 0
        temp = self.head
        
        while temp.next != None:
            leng += 1
            temp = temp.next

        return leng

    def add(self, data, index=0):
        new_node = Node(data)

        if index = 0:
            new_node.next = self.head
            self.head = new_node
            
        elif index >= self.length():
            temp = self.head
        
            while temp.next != None:
                leng += 1
                temp = temp.next

            temp.next = new_node

    def show(self):
        temp = self.head

        while temp.next != None:
            print(temp.data)
            temp = temp.next

        
