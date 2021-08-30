class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
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

    def append(self, data):
        '''
            We won't use insert() here because that would be O(n).
            Using a tail variable, we have reduced this insertion to O(1).
        '''

        if self.head:
            new_node = Node(data)

            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        else:
            # this is also O(1)
            self.insert(data, 0)
            self.tail = self.head

    def prepend(self, data):
        self.insert(data)

    def remove(self, index=0):
        if index == 0:
            temp = self.head
            self.head = self.head.next
            del temp

            self.length -= 1

            if self.length == 0:
                self.tail = self.head

        else:
            temp = self.head
            count = 0

            while temp != None and count != index:
                prev = temp
                temp = temp.next
                count += 1

            else:
                if count == index:
                    if temp != None:
                        prev.next = temp.next

                        if temp == self.tail:
                            self.tail = prev

                        del temp
                        self.length -= 1
                
                
    def show(self):
        temp = self.head
        l = []
        
        while temp != None:
            l.append(temp.data)
            temp = temp.next

        print(l)

        
