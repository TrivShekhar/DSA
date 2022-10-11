n,m=map(int,input().split())
arr = list(map(int,input().split()))
dic={}
for i in arr:
    dic[i]=dic.get(i,0)+1
arr = list(dic.values())
arr.sort()
print(arr[-n]*n)

