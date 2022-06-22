def endOfMaze(n: int, m: int, k: int) -> int:
    a=[[0]*m for i in range(n)]
    for i in range(0,n):
        for j in range(0,m):
            if(i+1<n):
                if(a[i+1][j]==0):
                    a[i+1][j]=(j+1)*k
            if(j+1<m):
                if(a[i][j+1]==0):
                    a[i][j+1]=(i+1)*k
    cost=0
    print(a)
    i=0
    j=0
    while(i+1!=n and j+1!=m):
        if(a[i+1][j]<=a[i][j+1]):
            cost+=a[i+1][j]
            i=i+1
        elif(a[i][j+1]<a[i+1][j]):
            cost+=a[i][j+1] 
            j=j+1
        elif(i==n-1 and j==m-1):
            break
    if(i+1==n):
        while(j+1!=m):
            cost+=a[i][j+1]
            j+=1
    if(j+1==m):
        while(i+1!=n):
            cost+=a[i+1][j]
            i+=1
    return cost
m,n,k=map(int,input().split())
endOfMaze(m,n,k)