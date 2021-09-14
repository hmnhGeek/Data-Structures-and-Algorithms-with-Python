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
            currentNode = node
            parentNode = None

            while currentNode.left != None:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                return currentNode

    def deleteNode(self, root, data):
        key = data

        # Base Case
        if root is None:
            return root
    
        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
    
        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(key > root.data):
            root.right = self.deleteNode(root.right, key)
    
        # If key is same as root's key, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.find_min(root.right)
    
            # Copy the inorder successor's
            # content to this node
            root.data = temp.data
    
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.data)
    
        return root

    def bf_traversal(self):
        currentNode = self.root

        bf_list = []
        queue = [currentNode,]

        while len(queue):
            currentNode = queue.pop(0)
            bf_list.append(currentNode.data)

            if currentNode.left:
                queue.append(currentNode.left)

            if currentNode.right:
                queue.append(currentNode.right)

        return bf_list

    def bf_traversal_recursive(self, queue, l):
        if not len(queue):
            return l

        currentNode = queue.pop(0)
        l.append(currentNode.data)

        if currentNode.left:
            queue.append(currentNode.left)

        if currentNode.right:
            queue.append(currentNode.right)

        return self.bf_traversal_recursive(queue, l)

    def dfs_inorder(self, node, l):
        if node.left:
            self.dfs_inorder(node.left, l)

        l.append(node.data)

        if node.right:
            self.dfs_inorder(node.right, l)

        return l

    def dfs_preorder(self, node, l):
        l.append(node.data)

        if node.left:
            self.dfs_preorder(node.left, l)

        if node.right:
            self.dfs_preorder(node.right, l)

        return l

    def dfs_postorder(self, node, l):
        if node.left:
            self.dfs_postorder(node.left, l)

        if node.right:
            self.dfs_postorder(node.right, l)

        l.append(node.data)
        return l

