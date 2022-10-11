from dataclasses import replace


def ReplaceWithProduct(arr):
    if(arr == None):
        return None
    for k,val in enumerate(arr):
        sl=0
        sr=0
        for i in range(k,len(arr)):
            if(arr[i]<val):
                sl+=arr[i]
            elif(arr[i]>val):
                sr+=arr[i]
        arr[k] = sl*sr
    return arr
print(ReplaceWithProduct([8,4,5,3,2,6,9,1]))