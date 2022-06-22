from BinaryTree import BinaryTree 
import random
bt=BinaryTree(1)
for i in range(10):
    bt.insert(bt.getroot(),random.randint(0,100))
bt.inorder(bt.getroot())