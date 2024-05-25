# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.nref=None
#
# class stack:
#     def __init__(self):
#         self.head=None
#
#     def printLinkedList(self):
#         n=self.head
#         if n is None:
#             print("there is no elemnt")
#         else:
#             while n is not None:
#                 print(n.data,"-->",end="")
#                 n=n.nref
#
#     def push(self,data):
#         n=self.head
#         newnode=Node(data)
#         newnode.nref=self.head
#         self.head=newnode
#
#     def pop(self):
#         if self.head is None:
#             print("there is no element to delete")
#         else:
#             self.head=self.head.nref
#
# link=stack()
# link.push(30)
# link.push(20)
# link.push(10)
# link.pop()
# link.printLinkedList()

#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#
# # Create a stack instance
# stack = Stack()
#
# # Push elements into the stack
# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# # Get the top element of the stack
# print("Top element:", stack.peek())  # Output: Top element: 30
#
# # Pop elements from the stack
# print("Popped:", stack.pop())        # Output: Popped: 30
# print("Popped:", stack.pop())
#




class stack:
    def __init__(self):
        self.item=[]

    def push(self,data):
        self.item.append(data)

    def emptyStack(self):
        return len(stack) == 0

    def pop(self):
        if self.emptyStack():
            print("there is Nothing to delete")
        else:
            return self.item.pop()





    def printSTACK(self):
        print(self.item.data)

