class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def length(self):
        leng = 0
        temp = self.head
        
        while temp.next != None:
            leng += 1
            temp = temp.next

        return leng

    def insert(self, data, index=0):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
        else:
            temp = self.head
            count = 0

            while count != index and temp != None:
                prev = temp
                temp = temp.next

                count += 1

            else:
                new_node.next = temp
                prev.next = new_node
                self.length += 1
                
    def show(self):
        temp = self.head
        l = []
        
        while temp != None:
            l.append(temp.data)
            temp = temp.next

        print(l)

        
