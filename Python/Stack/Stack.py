import random
class Stack:
    def __init__(self):
        self.stackli = [0]*10
        self.top = -1
    def push(self, data):
        if self.isfull():
            print("Stack overflow")
        else:
            self.top=self.top + 1
            self.stackli[self.top] = data
    def pop(self):
        if self.isempty():
            print("Stack underflow")
        else:
            data = self.stackli[self.top]
            self.top=self.top-1
            return data    
    def peek(self):
        if self.isempty():
            print("Stack Underflow")
        else:
            return self.stackli[self.top]
    def isfull(self):
        if self.top == 9:
            return True
        else:
            return False
    def isempty(self):
        if self.top == -1:
            return True
        else: 
            return False
st = Stack()
n = int(input("enter the number of element to push"))
for i in range(n):
    st.push(random.randint(1,100))
print(st.stackli)
print(st.pop())
print(st.pop())
print(st.peek())

