from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            return False

tree = BST()
for i in range(100):
    tree.insert(randint(0, 100))

# print(tree.root.data)

def traverse(root):
    if root:
        traverse(root.left)
        print(root.data)
        traverse(root.right)

traverse(tree.root)
