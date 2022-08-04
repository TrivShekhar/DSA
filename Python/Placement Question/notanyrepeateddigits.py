n1,n2=map(int,input().split())
count=0
for number in range(n1,n2+1):
    digits={}#dictionary
    repeated=False
    while(number>0):
        if(digits.get(number%10,0)==0):
            digits[number%10]=1
            number=number//10
        else:
            repeated=True
            break
    if(not repeated):
        count+=1
print(count)


