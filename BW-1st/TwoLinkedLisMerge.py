class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
    
class linkedist:
    def __init__(self):
        self.head = None

    def add(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = newnode

    def print(self):
        if self.head is None:
            print('nooo')
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end="")
            n = n.nref

    def oddDelete(self):
        n = self.head
        while n.nref is None:
            if n.data % 2 == 0 :
                n.nref = n.nref
            n = n.nref

ll = linkedist()
ll.add(21)
ll.add(22)
ll.add(23)
ll.add(24)
ll.add(25)
ll.add(26)
ll.add(27)
ll.print()
