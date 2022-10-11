class Node:
    def __init__(self,data=0):
        self.val=data
        self.left=None
        self.right=None
class BST:
    root=None
    def insert(self,val):
        if(self.root==None):
            self.root = Node(val)
            return
        temp=self.root
        while(temp!=None):
            if(temp.val<val):
                if(temp.right==None):
                    temp.right=Node(val)
                    return
                temp = temp.right
            else:
                if(temp.left==None):
                    temp.left=Node(val)
                    return 
                temp=temp.left
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)
tree=BST()
tree.insert(10)

tree.insert(5)

tree.insert(15)

tree.insert(2)

tree.insert(4)

tree.insert(12)

tree.inorder(tree.root)

        




