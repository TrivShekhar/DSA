

def countdig(i,y):
    count=1
    while(i>0):
        i=i//y
        count+=1
    return count
        

n,y= map(int,input().split())
coun=0
for i in range(n):
    coun+=countdig(i,y)
print(coun)

