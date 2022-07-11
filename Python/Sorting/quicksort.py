def partition(arr,left,right):
    i=left
    j=right-1
    piv=arr[right]
    while(i<j):
        while i<right and arr[i]<piv:
            i+=1
        while j>left and arr[j]>=piv:
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
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