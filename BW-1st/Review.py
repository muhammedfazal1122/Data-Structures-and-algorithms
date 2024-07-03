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


# class Node:
#     def __init__(self,key,value) -> None:
#         self.key = key
#         self.value = value
#         self.next = None

# class SeperateChaning:
#     def __init__(self,size) -> None:
#         self.arr = [None] * size
#         self.size = size
    
#     def hash_function(self,key):
#         return hash(key) % self.size

#     def insert(self,key,value):
#         index = self.hash_function(key)
#         if self.arr[index] is None:
#             self.arr[index] = Node(key,value)
#         else:
#             curr = self.arr[index]
#             while curr.next:
#                 curr = curr.next
#             curr.next = Node(key,value)
                

# class var:

#     hello = "helooo"
    

#     def __init__(self) -> None:
#         self.public = "im public"
#         self.__pri = "im private"
    


    
    
#     def ddddddddd(self):
#         print(self.hello)
#         self.__pri = "updated pri"
#         print(self.__pri)


# v = var()
# print(v.public)
# # print(v.__pri)
# v.ddddddddd()




# class Animal:
#     def sound(slef):
#         return "Animal sound"
    
# class Dog(Animal):
#     def sound(slef):
#         return "Dog sound"

# class Cat:
#     def sound(slef):
#         return "meoww"
    

# ss = Animal()
# print(ss.sound())
# dd = Dog()
# print(dd.sound())

# sss = "HEWFFFFFd"
# big = 0
# small = 0

# for i in sss:
#     if i.isupper():
#         big += 1
#     elif i.islower():
#         small += 1

# print(big)
# print(small)

# num = "123456789"

# def rev(num):
#     if len(num) == 1:
#         return num
    
#     return rev(num[1:]) + rev(num[0])

# print(rev(num))
    




# def rev(k):
#     if len(k) == 1:
#         return k
#     for i in k:
#         if type(i) == list:
            
#             return rev(k)
#         else:
#             k[::-1]
#     return k

# rr = rev(k)

# k = [[1, 2], [3, [4, 5]], 6]

# k = [[1, 2], [3, [4, 5]], 6]

# def rever(k):
#     return [rever(i) if isinstance(i, list) else i for i in k[::-1]]

# print(rever(k))




# def rever(k):
#     # Initialize an empty list to hold the results.
#     result = []
#     # Iterate over the reversed list.
#     for i in k[::-1]:
#         # If the current element is a list, recursively process it.
#         if isinstance(i, list):
#             result.append(rever(i))
#         # If the current element is not a list, simply append it to the result.
#         else:
#             result.append(i)
#     # Return the processed and reversed list.
#     return result


# # Example usage
# k = [[1, 2], [3, [4, 5]], 6]
# print(rever(k))


# s = "xoxyyoyydfgwdfopkpofdf"


# def is_palindrom(k):
#     return k == k[::-1]

# count = 0 
# res = []
# for i in range(len(s)):
#     for j in range(i+3, len(s)+1):
#         if is_palindrom(s[i:j]):
#             count  += 1
        


# print(count)

# class MyClass:
#     @property
#     def readonly_property(self):
#         return 42
# my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# filtered_dict = { key:values  for key , values in my_dict.items() if key[0] not in "aeiou" }



# print(filtered_dict)
# import random
# otp = ""
# def DoestRepeattheSameCharacterMorethan2TimesConsecutively(x,y):
#     res = [random.randint(x,y)]
#     for i in res:
#         if res.count(i)>3:
#                 res = [random.randint(x,y)]
#         else:
#              return otp = ''.join(res)
#     return otp = ''.join(res)




# print(DoestRepeattheSameCharacterMorethan2TimesConsecutively(100000,999999))





# def mergersort(arr):

#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#         mergersort(left)
#         mergersort(right)

#         i=j=k=0

#         while i < len(left) and j < len(right):
#             if left[i] < right[ j]:
#                 arr[ k ] = left[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1 
#                 k += 1 
        
#         while i < len(left):
#             arr[ k ] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1 
#             k += 1 

# bb= mergersort(arr)
# print(arr)


arr = [3,4,32,7,8,9,23,221,45,6,67,78,9,6754,3]



def pivote_place(arr,first,last):
    pivot = arr[first]
    left  = first +1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left > right:
            break
        arr[left],arr[right] = arr[right], arr[left]
    arr[right],arr[first] = arr[first],arr[right]
    return right

def Quick_sort(arr, first ,last):
    if first < last:
        p = pivote_place(arr, first , last)
        Quick_sort(arr, first, p-1)  
        Quick_sort(arr, p +1 , last)  
    
n = len(arr)-1
Quick_sort(arr, 0 , n)
print(arr)