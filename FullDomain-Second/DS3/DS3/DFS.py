graph={}
def add_list(v):
    if v in graph:
        print(v,'is present ')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'not present')
    elif v2 not in graph:
        print(v2, 'not present')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete(v):
    if v not in graph:
        print(v,'is not present')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)


def dfs(node,graph):
    visited=set()
    if node not in graph:
        print('node not present')
        return
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

def dfs_recurtion(node,graph):
    visited = set()
    if node not in graph:
        print("noo")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs_recurtion(i,graph)




add_list("a")
add_list("b")
add_list("c")
add_edge("a","b")
add_edge("a","c")
add_edge("b","c")
# delete("a")
dfs("a",graph)
# print(graph)





####...................................Function to perform BFS.

# def bfs(graph, start):
#     visited = set()          # To keep track of visited nodes.
#     queue = []               # Initialize a queue as a list.
#     queue.append(start)      # Enqueue the starting node.
#
#     while queue:
#         node = queue.pop(0)  # Dequeue the first node from the list.
#         if node not in visited:
#             print(node)      # Process the node (you can modify this part).
#             visited.add(node) # Mark the node as visited.
#
#             # Add adjacent unvisited nodes to the list.
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
# # Call BFS starting from node 'A'.
# print("BFS traversal starting from 'A':")
# bfs(graph, 'A')
