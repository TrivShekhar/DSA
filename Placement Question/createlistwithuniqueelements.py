li=input().split()
dic={}
for i in li:
    dic[i]=dic.get(i,0)+1
li=[]
for i in dic.keys():
    if dic[i]==1:
        li.append(i)
print(li)
