n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr=arr[::-1]
i=0
j=arr[0].index(max(arr[0]))
sum=0
while(i<n):
    sum+=arr[i][j]
    if(j+1<n and i+1<n):
        if(arr[i+1][j+1]<arr[i+1][j]):
            if(j-1>=0):
                if(arr[i+1][j-1]>arr[i+1][j]):
                    j=j-1
        else:
            if(j-1>=0):
                if(arr[i+1][j-1]>arr[i+1][j+1]):
                    j=j-1
                else:
                    j=j+1
            else:
                j=j+1
    elif(j-1>=0 and i+1<n):
            if(arr[i+1][j-1]>arr[i+1][j]):
                j=j-1
            else:
                j=j

    i+=1
print(sum)        


    




