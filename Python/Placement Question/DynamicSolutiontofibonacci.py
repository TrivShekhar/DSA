#this is a dynamic solution to fibonacci series
def fib(n,memo):
    if(memo==None):
        memo=[-1]*(n+1)
    
    if(memo[n]!=-1):
        return memo[n]
    if(n==1 or n==2):
        result = 1
    else:
        result = fib(n-2,memo)+ fib(n-1,memo)
    memo[n]=result
    return result


print(fib(10,None))