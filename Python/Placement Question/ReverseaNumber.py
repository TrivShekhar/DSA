num=int(input())
dig=0
i=-1
sum=0
tempnum=num
while(tempnum!=0):
    dig = tempnum%10
    tempnum//=10
    i+=1
while(num!=0):
    dig = num%10
    num//=10
    if(i%2==0):
        sum+=dig
    i-=1
print(sum)