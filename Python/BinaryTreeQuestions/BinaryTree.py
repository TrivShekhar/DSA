class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        self.data
        return str(self.data)
class BinaryTree:
    def __init__(self,data):
        self.root=Node(data)
    def insert(self,node,data):
        if node.data>data:
            if node.left:
                self.insert(node.left,data)
            else:
                node.left=Node(data)
        if node.data<data:
            if node.right:
                self.insert(node.right,data)
            else:
                node.right=Node(data)
    def getroot(self):
        return self.root
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
