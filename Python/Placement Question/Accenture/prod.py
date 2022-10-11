def productArray(arr):
    prod=1
    ansarr=[]
    for i in range(len(arr)):
        prod=1
        for j in range(len(arr)):
            if(i==j):
                continue
            prod*=arr[j]
        ansarr.append(prod)
    return ansarr

