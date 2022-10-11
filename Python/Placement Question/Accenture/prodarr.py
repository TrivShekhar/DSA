m , num = input().split()
m , num =  int(m),int(num)
found = True
mindis=999999999
number=m*2
i=2
while(found):
    tempmin = abs(num-number)
    if(tempmin>mindis):
        print(number-m)
        break
    else:
        mindis = tempmin
    i+=1
    number=m*i
    
    
    

    
