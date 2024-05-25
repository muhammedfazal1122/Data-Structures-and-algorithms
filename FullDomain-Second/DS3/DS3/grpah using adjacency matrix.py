# graph=[]
# node=[]
# node_count=0
#
# def add_node(v):
#     global node_count
#     if v in node:
#         print(v,"is present in the graph")
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=' ')
#         print()
#
# print('before adding value ')
# print(node)
# print(graph)
# print('after adding value')
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# print(node)
# print(graph)
# print_graph()
#
#

# node=[]
# graph=[]
# node_count=0
# def add_node(v):
#     global node_count
#     if v in graph:
#         print(v,"is already present")
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j], end=' ')
#         print()
#
#
# print('before adding')
# print(node)
# print(graph)
# print('after adding')
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# print(node)
# print(graph)
# print_graph()


# node=[]
# graph=[]
# node_count=0
# def add_node(v):
#     global node_count
#     if v in node:
#         print('node is present')
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=' ')
#         print()
#
# def add_edge(v1,v2):
#     if v1 not in node:
#         print(v1,"not present")
#     elif v2 not in node:
#         print(v2,"not present")
#     else:
#         index1=node.index(v1)
#         index2=node.index(v2)
#         graph[index1][index2]=1
#         graph[index2][index1]=1
#
#
# print('add before')
# print(node)
# print(graph)
# print('add after')
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# print(node)
# print(graph)
# add_edge("a","b")
# add_edge("b","d")
# print_graph()

# node=[]
# graph=[]
# node_count=0
# def add_node(v):
#     global node_count
#     if v in node:
#         print('v is present')
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=' ')
#         print()
#
#
# def add_edge(v1,v2):
#     if v1 not in node:
#         print(v1,"not present")
#     elif v2 not in node:
#         print(v2,"not present")
#     else:
#         index1=node.index(v1)
#         index2=node.index(v2)
#         graph[index1][index2]=1
#         graph[index2][index1]=1
#
#
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# print(node)
# print(graph)
# add_edge("a","d")
# add_edge("c","b")
# print_graph()
#
#

###............................................Adjency list.......

# graph={}
# def add_node(v):
#     if v in graph:
#         print(v,'is present ')
#     else:
#         graph[v]=[]
#
# add_node("a")
# add_node("b")
# add_node("c")
# print(graph)
#
#

# graph={}
# def add_node(v):
#     if v  in graph:
#         print(v,'is present')
#     else:
#         graph[v]=[]
#
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,'not present')
#     elif v2 not in graph:
#         print(v2,'not present')
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# add_edge("a","b")
# add_edge("b","d")
# print(graph)


# graph={}
# def add_node(v):
#     if v in graph:
#         print('node is present')
#     else:
#         graph[v]=[]
#
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print('not present')
#     elif v2 not in graph:
#         print(v2,'not present')
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
# add_node("a")
# add_node("b")
# add_node("c")
# print(graph)
# add_edge("a","b")
# add_edge("c","a")
# print(graph)

###.........................................Delete graph adjecency matrix..........

# node=[]
# graph=[]
# node_count=0
# def add_node(v):
#     global node_count
#     if v in node:
#         print(v,'is present')
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=" ")
#         print()
#
# def add_edge(v1,v2):
#     if v1 not in node:
#         print(v1,'not present')
#     elif v2 not in node:
#         print(v2,'not present')
#     else:
#         index1=node.index(v1)
#         index2=node.index(v2)
#         graph[index1][index2]=1
#         graph[index2][index1]=1
#
# def delete(v):
#     global node_count
#     if v not in node:
#         print(v,'not present')
#     else:
#         index=node.index(v)
#         node_count=node_count-1
#         node.remove(v)
#         graph.pop(index)
#         for i in graph:
#             i.pop(index)
#
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# print(graph)
# print(node)
# add_edge("a","b")
# delete("a")
# print_graph()
#

##############........................Adjecency list

# graph={}
# def add_node(v):
#     if v in graph:
#         print(v,'is present')
#     else:
#         graph[v]=[]
#
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"not present")
#     elif v2 not in graph:
#         print(v2,'not present')
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
# def delete(v):
#     if v not in graph:
#         print(v,'not present')
#     else:
#         graph.pop(v)
#         for i in graph:
#             list=graph[i]
#             if v in list:
#                 list.remove(v)
#
#
# add_node("a")
# add_node("b")
# add_node("c")
# add_edge("a","b")
# print(graph)
# delete("a")
# print()
# print(graph)
#
#
#
###################..................adjecency matrix
# graph={}
# def add_node(v):
#     if v in graph:
#         print(v,'already present')
#     else:
#         graph[v]=[]
#
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,'not present')
#
#     elif v2 not in graph:
#         print(v2,'not present')
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
# def delete(v):
#     if v not in graph:
#         print(v,'not present')
#     else:
#         graph.pop(v)
#         for i in graph:
#             list=graph[i]
#             if v in list:
#                 list.remove(v)
# add_node("a")
# add_node("b")
# add_node("c")
# print(graph)
# add_edge("a","b")
# print(graph)
# delete("c")
# print(graph)

# graph=[]
# node=[]
# node_count=0
# def add_node(v):
#     global node_count
#     if v in node:
#         print('node exsist')
#     else:
#         node_count+=1
#         node.append(v)
#         for n in graph:
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
#
# def add_edge(v1,v2):
#     if v1 in graph:
#         print(v1,'is present')
#     elif v2 in graph:
#         print(v2,'not prsent')
#     else:
#         index1=node.index(v1)
#         index2=node.index(v2)
#         graph[index1][index2]=1
#         graph[index2][index1]=1
#
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=' ')
#         print()
#
# def delete(v):
#     global node_count
#     if v not in node:
#         print('node not present')
#     else:
#         index1=node.index(v)
#         node_count-=1
#         node.remove(v)
#         graph.pop(index1)
#         for i in graph:
#             i.pop(index1)
#
# add_node("a")
# add_node("b")
# add_node("c")
# add_node("d")
# add_edge("a","c")
#
# delete("a")
# print(node)
# print(graph)
#
# print_graph()

#333333333333333333333...............3...................list

# graph={}
# def add_list(v):
#     if v in graph:
#         print(v,'is present ')
#     else:
#         graph[v]=[]
#
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,'not present')
#     elif v2 not in graph:
#         print(v2, 'not present')
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#
# def delete(v):
#     if v not in graph:
#         print(v,'is not present')
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1=graph[i]
#             if v in list1:
#                 list1.remove(v)
#
# add_list("a")
# add_list("b")
# add_list("c")
# add_edge("a","b")
# delete("a")
# print(graph)

