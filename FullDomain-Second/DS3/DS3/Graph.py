class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, v):
        if v in self.graph:
            print(v, "already present")
        else:
            self.graph[v] = []# This line adds node v to graph's dictionary(self.graph) as a key and assigns empty list[] as value.
                              #This empty list will represent the edges (connections) associated with this node.

    def delete_node(self, v):
        if v not in self.graph:
            print(v, "not present")
        else:
            self.graph.pop(v)
            for k in self.graph:
                list1 = self.graph[k]
                list1.remove(v)

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            print(v1, "not present")
        elif v2 not in self.graph:
            print(v2, "not present")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def del_edge(self, v1, v2):
        if v1 not in self.graph:
            print(v1, "not present")
        elif v2 not in self.graph:
            print(v2, "not present")
        else:
            if v1 in self.graph[v2]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)

g1 = Graph()
g1.add_node("A")
g1.add_node("B")
g1.add_node("C")
g1.add_edge("A", "B")
g1.add_edge("A", "C")
g1.add_edge("C", "B")
print(g1.graph)



class Graph:
    def __init__(self) :
        self.graph = {}

    def add_node(self,v):
        if v in self.graph:
            print("nooo")
        else:
            self.graph[v] = []

    def edghe_idser(self,v1,v2):
        if v1 not in self.graph:
            print("noo")
        elif v2 not in self.graph:
            print("no")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)


    def delete(self,v):
        if v not in self.graph:
            print("no")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1 = self.graph[i]
                if v in list1:
                    list1.remove(v)




gg = Graph()

gg.add_node(10)
gg.add_node(11)
gg.add_node(12)
gg.add_node(13)
gg.edghe_idser(12,10)
gg.edghe_idser(11,13)




print(gg.graph)


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
