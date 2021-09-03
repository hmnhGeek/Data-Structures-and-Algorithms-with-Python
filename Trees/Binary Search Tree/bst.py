class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        
        if not self.root:
            # if root is empty
            self.root = new_node

        else:
            currentNode = self.root

            while 1:
                if currentNode.data > data:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = new_node
                        return
                else:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = new_node
                        return

    def lookup(self, data):
        currentNode = self.root

        while currentNode != None:
            if data < currentNode.data:
                currentNode = currentNode.left
            elif data > currentNode.data:
                currentNode = currentNode.right
            else:
                return currentNode

    def jsonify(self, node):
        tree = {'left': node.left, 'value': node.data, 'right': node.right}

        tree['left'] = self.jsonify(node.left) if node.left else None
        tree['right'] = self.jsonify(node.right) if node.right else None

        return tree

    def is_leaf_node(self, node):
        return not node.left and not node.right

    def find_min(self, node):
        if node is not None:
            currentNode = self.root
            parentNode = None

            while currentNode.left != None:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                return parentNode, currentNode

    def delete(self, data):
        parentNode = None
        currentNode = self.root
        print(self.root.data)
        print("Current ", currentNode.data)

        while currentNode != None:
            print(currentNode.data)
            parentNode = currentNode

            if data > currentNode.data:
                currentNode = currentNode.right
            elif data < currentNode.data:
                currentNode = currentNode.left
            else:
                # we found the node

                if self.is_leaf_node(currentNode):
                    if parentNode.right == currentNode:
                        parentNode.right = None
                    else:
                        parentNode.left = None

                elif currentNode.left == None or currentNode.right == None:
                    if currentNode.left == None:
                        if currentNode.right.data < parentNode.data:
                            parentNode.left = currentNode.right
                        else:
                            parentNode.right = currentNode.right
                    else:
                        if currentNode.left.data < parentNode.data:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left

                else:
                    # has both children
                    parent_of_left_leaf_of_right, left_leaf_of_right = self.find_min(currentNode.right)
                    currentNode.data = left_leaf_of_right.data
                    parent_of_left_leaf_of_right.left = None
                    
bst = BinarySearchTree()
import random

for i in range(5):
    bst.insert(random.randint(1, 50))
    
print(bst.jsonify(bst.root))
