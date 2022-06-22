from BinaryTree import BinaryTree
import random
def depthfirstsearch(root):
    depthfirstsearch.stack.append(root)
    while(len(depthfirstsearch.stack)!=0):
        node = depthfirstsearch.stack.pop()
        print(node.data)
        if(node.right!=None):
            depthfirstsearch.stack.append(node.right)
        if(node.left!=None):
            depthfirstsearch.stack.append(node.left)
depthfirstsearch.stack=[]    
    

bt=BinaryTree(1)
for i in range(10):
    num=random.randint(0,100)
    print(num,end=" ")
    bt.insert(bt.getroot(),num)
bt.inorder(bt.getroot())
print()
depthfirstsearch(bt.getroot())
