def addnode(v):
    global node_count
    if v in nodes:
        print(v,'v is already present')
    else:
        node_count=node_count+1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def printgraph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()

nodes=[]
graph=[]
node_count=0

print('before adding nodes')
print(nodes)
print(graph)

addnode("a")
addnode("b")

print('after adding nodes')
print(nodes)
print(graph)


