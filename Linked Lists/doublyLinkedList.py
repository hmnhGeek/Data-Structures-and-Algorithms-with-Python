# DOUBLY LINKED LIST

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.len = 0

    def insert(self, data, index=0):
        new_node = Node(data)

        if self.head:

            if index == 0:
                new_node.next = self.head
                self.head.prev = new_node

                self.head = new_node
                self.head.prev = None

            else:
                count = 0
                temp = self.head
                
                while count != index and temp != None:
                    temp = temp.next
                    count += 1

                else:

                    if count == index and temp != None:
                        previous_node_of_temp = temp.prev

                        previous_node_of_temp.next = new_node
                        new_node.prev = previous_node_of_temp

                        new_node.next = temp
                        temp.prev = new_node

                    else:
                        # add to the end
                        self.tail.next = new_node
                        new_node.prev = self.tail

                        self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node


        self.len += 1

    def append(self, data):
        self.insert(data, self.len)

    def info(self):
        return {"head": self.head.data, "tail": self.tail.data, "length": self.len}

    def show(self):
        temp = self.head
        arr = []

        while temp != None:
            arr.append(temp.data)
            temp = temp.next

        return arr


dl = DoublyLinkedList()

dl.insert(100)
dl.insert(1000)
dl.insert(-10)

print(dl.show())
