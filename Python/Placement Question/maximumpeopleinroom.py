arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
depart = {}
arrive = {}
for i in arr:
    arrive[i[0]]+=1
    depart[i[1]]+=1
room = 0
time = arr[0][0]
endtime = max(arr,key = lambda a : a[1])
while time<=endtime:
    if ( time in arrive):
        room+=arrive[time]
    if(time in depart):
        room-= depart[time]
    time+=1

    