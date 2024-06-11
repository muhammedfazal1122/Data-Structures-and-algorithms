# class binarySerchTree:
#     def __init__(self,key):
#         self.key=key
#         self.lchild=None
#         self.rchild=None

#     def insert(self,data):
#         if self.key is None:
#             self.key=data
#             return
#         if self.key==data:
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild=binarySerchTree(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild=binarySerchTree(data)

#     def search(self,data):
#         if self.key == data:
#             print("found")
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("there is no value")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("there is also no value mahn")

#     def preOrderTraversal(self):
#         print(self.key,end=" ")
#         if self.lchild:
#             self.lchild.preOrderTraversal()
#         if self.rchild:
#             self.rchild.preOrderTraversal()

#     def inOrderTraversal(self):
#         if self.lchild:
#             self.lchild.inOrderTraversal()
#         print(self.key,end=" ")
#         if self.rchild:
#             self.rchild.inOrderTraversal()

#     def postOrderTraversal(self):
#         if self.lchild:
#             self.lchild.postOrderTraversal()
#         if self.rchild:
#             self.rchild.postOrderTraversal()
#         print(self.key,end=" ")

#     def delete(self, data):
#         if self.key is None:
#             print("there is no value")
#             return self

#         if self.key > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else:
#                 print("there is no value to delete left")
#         elif self.key < data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
#             else:
#                 print("there is no value to delete in right")
#         else:
#             if self.lchild is None:
#                 return self.rchild
#             if self.rchild is None:
#                 return self.lchild

#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)

#         return self


# root=binarySerchTree(10)
# list=[2,4,6,8,7,21,34,67,54,32]
# for i in list:
#     root.insert(i)

# # root.delete(724)
# # root.delete(739)
# # root.delete(754)
# # root.delete(777)
# # root.delete(71)
# # root.delete(73)
# # root.delete(72)
# # root.delete(21)
# # root.delete(32)
# root.delete(10)
# print("PreOrder")
# root.preOrderTraversal()

# print("\nInOrder")
# root.inOrderTraversal()

# print("\nPOSTorder")

# root.postOrderTraversal()


class BinarySerchTree:
    def __init__(self,key) :
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = BinarySerchTree(data)
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BinarySerchTree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BinarySerchTree(data)
    

    def serch(self,data):
        if self.key is None:
            print("no")
            return
        if self.key == data:
            print("found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.serch(data)
            else:
                print("no daat")
        else:
            if self.rchild:
                self.rchild.serch(data)
            else:
                print("no  data")


    def delete(self,data):
        if self.key is None:
            print("no data to dele")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("no data delete")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("no daa")
        else:
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    







    def inordertraversal(self):
        if self.lchild:
            self.lchild.inordertraversal()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inordertraversal()

root = BinarySerchTree(10)

list=[2,4,6,8,7,21,34,67,54,32]

for i in list:
    root.insert(i)

root.delete(3233)
root.inordertraversal()

# root.serch(3)
