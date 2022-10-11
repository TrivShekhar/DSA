graph={0:[1,3],1:[4,5],2:[5],3:[2],4:[2,5],5:[3]}
visited={}
def traverse(key):
    if(visited.get(key)):
        return
    print(key)
    visited[key]=1
    nodes = graph[key]
    for neighbour in nodes:
        traverse(neighbour)
for i in graph.keys():
    traverse(i)

