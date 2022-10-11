from itertools import combinations
n = int(input())
k = int(input())
count = 0
flavours = [i for i in range(1,n+1)]
def makecombination(arr,currc):
    global count
    count+=len(list(combinations(arr,currc)))
for i in range(n):
    for j in range(1,k):
        makecombination(flavours[i:],j)
print(count)
        





