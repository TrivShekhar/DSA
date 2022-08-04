def knapsack(weight,cost,target,i):
    if(target==0 or i==0):
        res=0
    elif(target<weight[i]):
        res=knapsack(weight,cost,target,i-1)
    else:
        tmp1=knapsack(weight,cost,target,i-1)
        tmp2=cost[i]+knapsack(weight,cost,target-weight[i],i-1)
        res = max(tmp1,tmp2)
    return res



weight=list(map(int,("0 " + input()).split()))
cost=list(map(int,("0 " + input()).split()))
target=int(input())
print(knapsack(weight,cost,target,len(weight)-1))