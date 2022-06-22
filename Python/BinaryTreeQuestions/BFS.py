from BinaryTree import BinaryTree
import random

def breadth_first_search(root):
    queue=[]
    front=0
    queue.append(root)
    while(front!=len(queue)):
        ele=queue[front]
        print(ele.data)
        if(ele.left!=None):
            queue.append(ele.left)
        if(ele.right!=None):
            queue.append(ele.right)
        front+=1
    
bt=BinaryTree(1)
for i in range(10):
    num=random.randint(1,100)
    print(num,end=" ")
    bt.insert(bt.getroot(),num)
bt.inorder(bt.getroot())
print()
breadth_first_search(bt.getroot())