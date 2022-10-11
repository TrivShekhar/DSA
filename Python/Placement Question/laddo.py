n = int(input())
perf= list(map(int,input().split()))
lado=[1]*n

for i in range(0,n):
    if(i==0):
        if(perf[i+1]<perf[i]):
            lado[i]=lado[i+1]+1
    elif(i==n-1):
        if(perf[i-1]<perf[i]):
            lado[i]=lado[i-1]+1
    else:
        if(perf[i] == max(perf[i-1],perf[i],perf[i+1])):
            lado[i]=lado[max([i-1,i+1],key= lambda ind : perf[ind])]+1
        elif(perf[i+1]<perf[i]):
            lado[i]=lado[i+1]+1
        elif(perf[i-1]<perf[i]):
            lado[i]=lado[i-1]+1

print(sum(lado))
    