#
# queue=[]
# def enqueue():
#     element=int(input("eneter the elements"))
#     queue.append(element)
#
#
# def dequeue():
#     s= queue.pop(0)
#     print('poped element is',s)
#
# def display():
#     print(queue)
#
# while True:
#     choice=int(input('enter the choice 1 enqueue 2 dequeue 3 display 4 quit'))
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         display()
#     else:
#         break
#

#...................................Queue with linked list.............................

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class queue:
#     def __init__(self):
#         self.next=None
#         self.prev=None
#
#     def enqueue(self,data):
#         newnode=node(data)
#         if self.next is None:
#             self.next=newnode
#             self.prev=newnode
#         self.next.ref=newnode
#         self.next=newnode
#
#     def dequeue(self):
#         self.prev=self.prev.ref
#
#     def display(self):
#         n=self.prev
#         while n is not None:
#             print(n.data,'-->',end=' ')
#             n=n.ref
#
#
# s=queue()
# s.enqueue(100)
# s.enqueue(200)
# s.enqueue(300)
# s.enqueue(400)
# s.enqueue(500)
# s.dequeue()
# s.display()

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class queue:
#     def __init__(self):
#         self.next=None
#
#     def enqueue(self,data):
#         newnode=node(data)
#         if self.next is None:
#             self.next=newnode
#             self.prev=newnode
#
#         self.next.ref=newnode
#         self.next=newnode
#
#     def display(self):
#         n=self.prev
#         while n is not None:
#             print(n.data,'-->',end='')
#             n=n.ref
#
#     def dequeue(self):
#         self.prev=self.prev.ref
#
# s=queue()
# s.enqueue(100)
# s.enqueue(200)
# s.enqueue(300)
# s.enqueue(400)
# s.enqueue(500)
# #s.dequeue()
# s.display()


# q1 = []
# q2 = []
#
# def push(v):
#     q2.append(v)
#     while q1:
#         q2.append(q1.pop(0))
#     q1.extend(q2)
#     q2.clear()
#
# def pop():
#     return q1.pop(0)
#
# def display():
#     print(q1)
#
# push(10)
# push(30)
# push(20)
# push(40)
# push(50)
# pop()
# display()
#


class QueueStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def enqueue(self, data):
        self.q2.append(data)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1.extend(self.q2)
        self.q2.clear()

    def dequeue(self):
        self.q1.pop(0)
        print(self.q1)

    def display(self):
        print(self.q1)


s = QueueStack()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(40)
s.display()
s.dequeue()










