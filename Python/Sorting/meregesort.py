
def mergesort(arr):
    lent=len(arr)
    if(lent>1):
        arr1=arr[:lent//2]
        arr2=arr[lent//2:]
        mergesort(arr1)
        mergesort(arr2)
        i=0
        j=0
        k=0
        while(i<len(arr1) and j<len(arr2) ):
            if(arr1[i]<arr2[j]):
                arr[k]=arr1[i]
                i+=1
            elif(arr2[j]<arr1[i]):
                arr[k]=arr2[j]
                j+=1
            # elif(arr1[i]==arr2[j]):
            #     arr[k],arr[k+1]=arr1[i],arr2[j]
            #     i+=1
            #     j+=1
            #     k+=1
            k+=1
        while(i<len(arr1)):
            arr[k]=arr1[i]
            i+=1
            k+=1
        while(j<len(arr2)):
            arr[k]=arr2[j]
            j+=1
            k+=1




arr=list(map(int,input().split()))
mergesort(arr)
print(arr)