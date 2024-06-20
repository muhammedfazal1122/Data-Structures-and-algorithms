class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def insert_node(self,node):
        if node in self.graph:
            print("alredu")
        self.graph[node] = []
    def insert_edge(self,v1,v2):
        if v1 not in self.graph:
            print("not a elemnt")
        elif v2 not in self.graph:
            print("not a elemnt")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def delete(self,v1):
        if v1 not in self.graph:
            print("fsadfasd")
        self.graph.pop(v1)
        for i in self.graph:
            list1 = self.graph[i]
            list1.remove(v1)






