# 10,20,30,40,50 
#k=2
# 40,50,10,20,30
arr=list(map(int,input().split()))
k=int(input())
k=k%len(arr)
ans=list()
i=(len(arr)-k)%len(arr)
while(i!=len(arr)-k-1):
    ans.append(arr[i])
    i=(i+1)%len(arr)
ans.append(arr[i])
print(ans)
