def partition(arr,left,right):
    i=left
    piv=arr[right]
    for j in range(left,right):
        if(piv>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[right]=arr[right],arr[i]
    return i


def quicksort(arr,left,right):
    if(left<right):
        part=partition(arr,left,right)
        quicksort(arr,left,part-1)
        quicksort(arr,part+1,right)


arr=list(map(int,input().split()))

quicksort(arr,0,len(arr)-1)
print(arr)