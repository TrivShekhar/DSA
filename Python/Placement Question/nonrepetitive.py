def nonrepetitive(N,arr,k):
    hmap = {}
    for i in arr:
        hmap[i] = hmap.get(i,0)+1
    cnt = 0
    for i in arr:
        if hmap[i]==1:
            cnt+=1
        if cnt==k:
            return i
print(nonrepetitive(9,[45623,1321,555555,23123,1321,56344,9999,11111],5))