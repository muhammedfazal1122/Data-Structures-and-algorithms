# def bubble(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#     return arr



#selectip 
# n = len(list1)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n-1):
#         if list1[min_index]>list1[j]:
#             min_index = j
#     if list1[min_index] != list1[i]:
#         list1[min_index],list1[i] = list1[i],list1[min_index]

# print(list1)


# i = 0
# while i<len(list1):
#     pos = i
#     while pos>0 and list1[pos]<list1[pos-1]:
#         list1[pos-1],list1[pos] = list1[pos],list1[pos-1]
#         pos -= 1
#     i += 1
# print(list1)





# def merge(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge(left)
#         merge(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#                 k += 1
#         while i<len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1 
#             k += 1

# merge(list1)  
# print(list1)


# def pivote(arr,first,last):
#     pivot  = list1[first]
#     left = first+1
#     right = last

#     while True:
#         while arr[left] <= pivot and left<=right  :
#             left = left+1
#         while  arr[right] >= pivot and left<=right :
#             right = right-1
#         if left>right:
#             break
#         arr[left],arr[right] = arr[right],arr[left]
#     arr[right],arr[first] = arr[first],arr[right]
#     return right
 
# def quocK(arr,first,last):
#     if first<last:
#         p =  pivote(arr,first,last)
#         quocK(arr,first,p-1)
#         quocK(arr,p+1,last)



# n = len(list1)-1
# quocK(list1,0,n)
# print(list1)



# class bst:
#     def __init__(self,key) -> None:
#         self.key = key
#         self.lchild = None
#         self.rchild = None


#     def insert(self, data ):
#         if self.key is None:
#             self.key = bst(data)
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = bst(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = bst(data)

#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key,end=" ")
#         self.clon(self.key)
#         if self.rchild:
#             self.rchild.inorder()



#     def clon(self,data):
#         if self.key is None:
#             self.key = bst(data)
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = bst(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = bst(data)





# bb = bst(10)
# bb.insert(11)
# bb.insert(12)
# bb.insert(13)
# bb.insert(14)
# bb.insert(15)

# bb.inorder()


class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None

class SeperateChaning:
    def __init__(self,size) -> None:
        self.arr = [None] * size
        self.size = size
    
    def hash_function(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index = self.hash_function(key)
        if self.arr[index] is None:
            self.arr[index] = Node(key,value)
        else:
            curr = self.arr[index]
            while curr.next:
                curr = curr.next
            curr.next = Node(key,value)
                


