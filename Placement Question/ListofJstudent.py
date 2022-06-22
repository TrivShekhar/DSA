li = input().split()
jlist = [x for x in li if x[0] in ["j","J"]]
print(jlist)
li = map(int,input().split())
di = { x:x**2 for x in li if x%2==1}
print(di)