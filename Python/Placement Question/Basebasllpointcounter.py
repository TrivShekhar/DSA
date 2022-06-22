points=input().split()
stack=[]
for i in points:
    if i=="c":
        stack.pop()
    elif i=="d":
        stack.append(stack[-1]*2)
    elif i=="+":
        stack.append(stack[-1]+stack[-2])
    else:
        stack.append(int(i))
    
print(sum(stack))

