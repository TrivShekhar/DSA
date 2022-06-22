class Heap:
    def __init__(self,data=[]):
        self._heap=data
        if(len(self._heap)>1):
            self.heapify()
    def insert(self,data):
        self._heap.append(data)
        if(len(self._heap)>1 and (self._heap[-1]>self._heap[-2])):
            self._heapify()
    def heapify(self):
        for i in range(len(self._heap),0,-1):
            if(self._heap[i-1]>self._heap[(i-1)//2]):    
                self._heap[(i-1)//2],self._heap[i-1]=self._heap[i-1],self._heap[(i-1)//2]
                self.heapify()
    def delete(self):
        if(len(self._heap)==1):
            self._heap = []
        else:
            self._heap[0] = self._heap.pop()
            self.heapify()
    def getmax(self):
        return self._heap[0]
heap = Heap([11,1,2,10,7,3,9,15])
print(heap._heap)
heap.delete()
print(heap._heap)


    
            
    
