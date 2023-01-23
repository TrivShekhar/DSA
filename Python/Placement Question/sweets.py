string = input()
llist = string.split("],")

ans = []
for i,val in enumerate(llist):
    if i < len(llist)-1:
        ans.append(eval(val+"]"))
    else:
        ans.append(eval(val))
print(ans)