import random
class Queue:
    def __init__(self):
        self.queueLi=[0]*9
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.isfull():
            print("Queue is full.")
        else:
            self.front=0
            self.rear=self.rear+1
            self.queueLi[self.rear]=data
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            data=self.queueLi[self.front]
            self.front=self.front+1
            return data
    def isfull(self):
        if self.rear==9:
            return True
        else:
            return False
    def isempty(self):
        if self.front==-1:
            return True
        else:
            return False
q=Queue()
n=int(input("Enter no. of elements to be inserted inside queue :"))
for i in range(n):
    q.enqueue(random.randint(1,100))
print(q.queueLi)
print(q.dequeue())
print(q.dequeue()) 
print(q.queueLi) 
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue())