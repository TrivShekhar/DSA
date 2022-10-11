graph={1:[4],2:[4],3:[1,2],4:[7,8],5:[1,4,6],6:[10,11],7:[9],8:[9,10],9:[12],10:[12,13],11:[10],12:[],13:[]}
a="abcdefghijklmnopqrstuvwxyz"
visited={}
topo=[]
def traverse(key):
    if(visited.get(key)):
        return
    visited[key]=1
    nodes = graph[key]
    for neighbour in nodes:
        traverse(neighbour)
    topo.append(a[key-1])
for i in graph.keys():
    traverse(i)
print("".join(topo).upper()[::-1])
