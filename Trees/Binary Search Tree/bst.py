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


bst = BinarySearchTree()
bst.insert(9)
bst.insert(10)
bst.insert(-1)
bst.insert(100)
bst.insert(2)
print(bst.jsonify(bst.root))
