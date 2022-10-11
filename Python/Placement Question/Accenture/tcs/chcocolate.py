n=int(input())
k = int(input())
k=[0]*k
arr=[]
for i in range(n):
    arr.append(list(map(int,(input().split()))))
arr.sort(key=lambda a: a[0])
arr.sort(key=lambda a: a[1]-a[0])
count=0
for i in arr:
    if(k[i[2]-1]==0 or k[i[2]-1]<=i[0]):
        count+=1
        k[i[2]-1]=i[1]
print(count)