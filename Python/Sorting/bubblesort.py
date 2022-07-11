arr=list(map(int,input().split()))
swapped = False
for i in range(len(arr)):
    
    for j in range(0,len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped= True
        print(arr)
    if not swapped:
        break
print(arr)
