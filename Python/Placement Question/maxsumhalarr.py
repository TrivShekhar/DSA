def maxSum(v1,v2):
    v1.sort()
    v2.sort()
    su=0
    for i in range(len(v1)):
        su+=v1[i]*v2[i]
    return su
print(maxSum([7,6,7,7,9],[6,8,7,9,0]))
