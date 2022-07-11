def ninjaAndSortedArrays(arr1,arr2,m,n):
    arr=[]
    i=0
    j=0        
    arr1=arr1[0:m]
    while(i<m and j<n):
        while(i<m and j<n and arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i+=1   
        while(i<m and j<n and arr2[j]<arr1[i]):
            arr.append(arr2[j])
            j+=1
        if(i<m and j<n and  arr1[i]==arr2[j]):
            arr.append(arr1[i])
            i+=1
            arr.append(arr2[j])
            j+=1
            if(j==n or i==m):
                break
    while(i<m):
        arr.append(arr1[i])
        i+=1
    while(j<n):
        arr.append(arr2[j])
        j+=1
    return arr
i,j=4,2
a=[2, 4, 6, 8, 0, 0]
b=[2, 9]


ninjaAndSortedArrays(a,b,i,j)