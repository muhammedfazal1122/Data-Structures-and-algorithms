# set1 = frozenset({1, 2, 3})
# set2 = frozenset({3, 4, 5})

# myset = {1,2,3,4,5}

# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1.difference(set2)
# symmetric_difference_set = set1.symmetric_difference(set2)
# print(intersection_set,union_set)
# arr1 = {1: "wer", 2: "fff", 3: "rrr"}
# arr2 = {3: 3, 4: 56, 12: 45}
# def is_palindrome(s):
#     return s == s[::-1]

# # Test
# print(is_palindrome("racecar"))  # Output: True
# f = "jsadssss fjddi enfdsndddd"
# name = (set(f))
# n = "".join(name)
# print(n)

# my_set = {'a', 'b', 'c'}
# my_string = ''.join(my_set)
# print(my_string) 

# name = ["fazal","fazal","sune"]
# age = [21,22,23]

# # lisrrrb  = list(zip(name,age))

# name[0] = "hello"
# print((name))

# numbers = [1, 2, 3, 4, 5]
# new_numbers = [list(filter(lambda i: i%2==0 , numbers))]
# print(new_numbers)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Example usage
# for i in range(10):
#     print(fibonacci(i))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Example usage
# for i in range(1, 6):
#     print(f"{i}! =", factorial(i))
# Example usage of zip()
# list1 = [1, 2, 3,4,5]
# list2 = ['a', 'b', 'c','d']
# zipped = zip(list1, list2)

# # Iterate over the zipped iterator
# for item in zipped:
#     print(item)
# # Example usage of enumerate()
# my_list = ['a', 'b', 'c', 'd', 'e']

# # Enumerate over the list and print each element along with its index
# for x, value in enumerate(my_list):
#     print(f"Index: {x}, Value: {value}")
# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print("Parent __init__ called")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Calling superclass constructor
#         self.age = age
#         print("Child __init__ called")

# child = Child("Alice", 10)
# print(child.name) 
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} created")
    
#     def __del__(self):
#         print(f"{self.name} destroyed")

# # Create an instance of MyClass
# obj = MyClass("Object")

# # The object is no longer in use
# del obj
def modify_value(x):
    x += 1
    print(x)

num = 5
modify_value(num)
# print(num)  # Output: 5
