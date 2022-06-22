import queue
class Stack:
    def __init__(self):
        self.queue1=queue.Queue()
        self.queue2=queue.Queue()
        self.curr_size=0
    def push(self,data):
        self.curr_size+=1
        self.queue1.put(data)
    def pop(self):
        i=0
        while(i<self.curr_size-1):
            self.queue2.put(self.queue1.get())
            i+=1
        val=self.queue1.get()
        temp = self.queue1 
        self.queue1 = self.queue2
        self.queue2 = temp
        self.curr_size-=1
        return val
    
st = Stack()
st.push(20)
st.push(30)
st.push(10)
st.push(40)
st.push(60)
st.push(70)
print(st.pop())
print(st.pop())
print(st.pop())






        

