arr=list(map(int,input().split()))
swapped = False
for i in range(len(arr)):
    minin=i
    for j in range(i+1,len(arr)):
        if arr[minin]>arr[j]:
            minin=j
    arr[i],arr[minin]=arr[minin],arr[i]
print(arr)