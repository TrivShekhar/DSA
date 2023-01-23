def chocolatesinbox(n,x):
    y = n-x
    while x>0 and y>0 and x!=y:
        if x>y:
            x-=y
        elif y>x:
            y-=x

    return n-x-y
print(chocolatesinbox(11,4))