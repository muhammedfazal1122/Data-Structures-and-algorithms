class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Queue:
    def __init__(self):
        self.head=None

    def print_Que(self):
        if self.head is None:
            print("there is no value to delte")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref


    def enQueue(self,data):
        n=self.head
        newnode= Node(data)
        newnode.ref=self.head
        self.head=newnode

    def deQueue(self):
        if self.head is None:
            print("ther is no value to delete ")
        else:
            n= self.head
            while n.ref is not None:
                n=n.ref
            n.ref = None



que=Queue()
que.enQueue(10)
que.enQueue(20)

que.deQueue()
que.print_Que()