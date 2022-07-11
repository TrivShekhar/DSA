def heapify(arr,i,n):
    m=i
    l = 2 * i + 1  
    r = 2 * i + 2
    if(n>l and arr[m]<arr[l]):
        m=l
    if(n>r and arr[m]<arr[r]):
        m=r
    if(m!=i):
        arr[m],arr[i]=arr[i],arr[m]
        heapify(arr,m,n)
def buildheap(arr):
    start=len(arr)//2-1
    for i in range(start,-1,-1):
        heapify(arr,i,len(arr))
def sort(arr):
    length=len(arr)-1
    while(length!=0):
        arr[0],arr[length]=arr[length],arr[0]
        heapify(arr,0,length)
        length-=1



arr=list(map(int,input().split()))
buildheap(arr)
sort(arr)
print(arr)
