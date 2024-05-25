class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        newnode=node(data)
        newnode.ref=self.top
        self.top=newnode

    def pop(self):
        self.top=self.top.ref

#     def display(self):
#         n=self.top
#         while n is not None:
#             print(n.data,"-->",end=" ")
#             n=n.ref
#
#
# s=stack()
# s.push(100)
# s.push(200)
# s.push(300)
# s.push(400)
# s.push(500)
# s.pop()
# s.display()

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
#
# class stack:
#     def __init__(self):
#         self.top=None
#
#     def push(self,data):
#         newnode=node(data)
#         newnode.ref=self.top
#         self.top=newnode
#
#     def pop(self):
#         self.top=self.top.ref
#
#     def display(self):
#         n=self.top
#         while n is not None:
#             print(n.data,'-->',end=' ')
#             n=n.ref
#
# s=stack()
# s.push(100)
# s.push(200)
# s.push(300)
# s.push(400)
# s.push(500)
# s.push(600)
# s.pop()
# s.display()
#
#

#..........................stack using array...............................


# class stack:
#
#     def stack(self):
#         stack=[]
#         for i in range(5):
#             element=int(input('enter elements'))
#             stack.append(element)
#             for i in stack:
#                 print(i)
#
#     def pop(self):
#             stack.pop(1)
#
#
# s=stack()
# s.stack()
# s.pop()
