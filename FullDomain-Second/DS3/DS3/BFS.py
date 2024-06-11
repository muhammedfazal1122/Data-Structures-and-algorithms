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


def bfs(node,graph):
    if node not in graph:
        print('not present')
        return
    visited=set()
    queue=[]
    queue.append(node)

    while queue:
        current=queue.pop(0)
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                if i not in visited:
                    queue.append(i)

add_list("a")
add_list("b")
add_list("c")
add_list("d")
add_edge("a","b")
add_edge("b","c")
add_edge("b","d")
add_edge("d","a")
bfs("a",graph)
