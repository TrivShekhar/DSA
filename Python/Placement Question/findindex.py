def findsum(a,n) -> int:
        temp = a[:]
        for i in range(1,len(a)):
            temp[i]+=temp[i-1]
        for i in range(1,len(a)-1):
            
            if temp[i-1] == temp[-1]-temp[i]:
                return temp[i-1]

def findelement(a,n) -> int:
        temp = a[:]
        for i in range(1,len(a)):
            temp[i]+=temp[i-1]
        for i in range(1,len(a)-1):
            
            if temp[i-1] == temp[-1]-temp[i]:
                return a[i]
