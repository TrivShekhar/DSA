def heapify(arr,n):
    left=n*2+1
    right=n*2+2
    maxi=n
    if(left<len(arr) and arr[left]>arr[maxi]):
        maxi=left
    if(right<len(arr) and arr[right]>arr[maxi]):
        maxi=right
    if(arr[maxi]>arr[n]):
        arr[maxi],arr[n]=arr[n],arr[maxi]
        heapify(arr,maxi)

def buildheap(arr):
    n=len(arr)
    start=n//2-1
    for i in range(start,-1,-1):
        heapify(arr,i)

arr=[34,65,7,82,3,6,2,93]
buildheap(arr)
print(arr)



    
            
    
