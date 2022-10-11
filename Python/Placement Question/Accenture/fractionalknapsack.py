a=[]
for i in range(3):
    a.append(int(input()))
for i in range(3):
    a[i] = [int(input()),a[i]]
lim = int(input())
a.sort(key= lambda x : x[0]/x[1] , reverse=True)
fval=0
for i in a:
    if(lim-i[1]>=0):
        fval+=i[0]
        lim-=i[1]
    else:
        fval+=i[0]*lim/i[1]
print(fval)

