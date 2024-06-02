# def bublesort(arr):
#     l = len(arr)
#     for i in range(l-1):
#         for j in range(l-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
# print(bublesort(list1))

# def mergesort(arr):
#     if len(arr)>1:
#         mid = len(arr)//2
#         leftarr = arr[:mid]
#         rightarr = arr[mid:]

#         mergesort(leftarr)
#         mergesort(rightarr)

#         i = k = j = 0

#         while i < len (leftarr)  and j < len(rightarr) :
#             if leftarr[i]<rightarr[j]:
#                 arr[k] = leftarr[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = rightarr[j]
#                 j += 1
#                 k += 1
#         while i < len(leftarr) :
#             arr[k] = leftarr[i]
#             i += 1
#             k += 1
#         while j < len(rightarr):
#             arr[k] = rightarr[j]
#             j += 1
#             k += 1

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
# (mergesort(list1))
# print(list1)


# def pivote(list1, first, last):
#     pivot = list1[first]
#     left = first+1
#     right = last


#     while left < right and list1[left] <  pivot:
#         left += 1
#     while left  < right and list1[left] > pivot:
#         right += 1
#     list1[left],list1[right] = list1[right],list1[left]
#     if left > right:
#         list1[right],list1[first] = list1[first],list1[right]
#     return right

# def quicksort(list1, first, last):
#     if first<last:
#         p = pivote(list1,first,last)
#         quicksort( list1,first, p-1)
#         quicksort( list1,p+1, last)

# l = len(list1)
# (quicksort(list1, 0 ,l))
# print(list1)


# l = len(list1)
# i = 0
# while i < l:
#     pos = i
#     while pos > 0 and  list1[pos]< list1[pos -1]:
#         list1[pos],list1[pos -1] = list1[pos -1], list1[pos]
        # pos -= 1 
#     i += 1 

# print(list1)

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
  
# for i in range(len(list1)-1):
#     min_intex = i
#     for j in range(i+1,len(list1)):
#         if list1[j]< list1[min_intex]:
#             min_intex = j
#     if list1[i]!=min_intex:
#         list1[i],list1[min_intex]=list1[min_intex],list1[i]

# print(list1)


# import pickle

# # Data to pickle
# data = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Pickle the data and save it to a file
# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)

# # Unpickle the data from the file
# with open('data.pickle', 'rb') as file:
#     loaded_data = pickle.load(file)

# print(loaded_data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

 


# even = [i*2 if i%2 == 0 else i*2 for i in nums ]

# i = 0
# j = len(nums)-1
# while i< len(nums)-1:
#     nums[i], nums[j] = nums[j], nums[i]
#     i += 1
#     j -= 1 
# c = "2" * 5



# def fun(nums):
#     nums.append(1212)
#     return nums
# nums = [10, 20, 30, 40, 50, 60]
# print(fun(nums) )
# print(nums)


# a = 10
# b = 10
# print(id(a))  # Output might be something like 140714030153776
# print(id(b))


# c = [1, 2, 3,3,5,6,89]
# print(id(c))



# with open("inheritance.py", "r") as file:
#     content = file.read()
#     print(content) 


num = [1,2,3,5,6,79,9]

# a = map([lambda:x*x ,num])

# c = lambda: x:2*x ,num

# def add(x):
#     return x*2

# v = map(add,num)
 
# print(list(v))

# num2 = [2,4,6,8,9]


# c = [lambda i:i *2 for i in range(len(num))]

# print(c)



# import copy

# # Original list with nested list
# original_list = [1, 2, [3, 4]]

# # Shallow copy of the original list
# shallow_copied_list = copy.copy(original_list)

# # Modifying the nested list in the shallow copy
# shallow_copied_list[1] = 'changed'

# print("Original List:", original_list)
# print("Shallow Copied List:", shallow_copied_list)  

# def jeee():
#         return 'ggggggggggggggggggggggg'

# class Anima:
    
#     def jeee(): 
#         return 'cxcvzxcvxzcv'


# print(Anima.jeee())


class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=5):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size



    def insert_item(self, key, value, i=0):
        index = self.hash_key(key)

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            while self.arr[index] is not None:
                i += 1
                index = (self.hash_key(key) + i ** 2) % self.size
            self.arr[index] = Node(key, value)


    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.key, ":", current.value, " --> ", end="")
                    else:
                        print(current.key, ":", current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()


class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=5):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size

    def insert_item(self, key, value):
        index = self.hash_key(key)

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            while self.arr[index] is not None:
                index = (index + 1) % self.size
            self.arr[index] = Node(key, value)


    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.key, ":", current.value, " --> ", end="")
                    else:
                        print(current.key, ":", current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()



class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=2):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size

    def insert_item(self, key, value):
        index = self.hash_key(key)

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            current = self.arr[index]    
            while current.ref:           
                current = current.ref
            current.ref = Node(key, value)

    def delete_item(self, key):
        index = self.hash_key(key)
        current = self.arr[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    # Deleting the head node
                    self.arr[index] = current.ref
                else:
                    # Deleting a node that is not the head
                    prev.ref = current.ref
                return True  # Key found and deleted
            prev = current
            current = current.ref

        return False  # Key not found

    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.value, " --> ", end="")
                    else:
                        print(current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()