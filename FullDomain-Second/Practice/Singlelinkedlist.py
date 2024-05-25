class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("There is no data")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end="")
                n = n.nref
    
    def addFirstnode(self, data):
        newnode = Node(data)
        newnode.nref = self.head 
        self.head = newnode

    def addbeforeelemenet(self, data, x):
        newnode = Node(data)
        if self.head is None:
            print("empty")
            return
        if self.head.data == x:
            newnode.nref = self.head
            self.head = newnode
            return
        n = self.head
        while n.nref is not None:
            if n.nref.data == x:
                newnode.nref = n.nref
                n.nref = newnode
                return
            n = n.nref
        print("Element not found")

obj = LinkedList()
    
obj.addFirstnode(40)
obj.addFirstnode(30)
obj.addFirstnode(20)
obj.addFirstnode(10)
obj.addbeforeelemenet(77, 40)

obj.print()



