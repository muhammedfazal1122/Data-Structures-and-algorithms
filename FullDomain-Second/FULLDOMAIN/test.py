# def fun(*a,**b):
#     return a+b
#
# s=fun(5,b=50)
# print(s)


# def fun(*a):
#     return sum(a)
# s=fun(5,1,4)
# print(s)

# def fun(**b):
#     return b
#
# s=fun(b=50,b=8)
#
# print(s)

# def fun(**b):
#     return b
#
# s=fun(b=10,c=22,v=33)
# print(s)

# l=lambda x,y:x+y
# s=l(5,6)
# print(s)
#
# people = [
#     {"name": "Alice", "age": 30, "location": "New York"},
#     {"name": "Charlie", "age": 35, "location": "Chicago"},
#     {"name": "Charlie", "age": 35},
#     {"name": "Eve", "age": 32}
# ]
# # print(f'name {}')
#
# for i in people:
#     print(i)
#
# class a:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def display(self):
#         print(self.b)
#
#
# def decorator(fun):
#     def method():
#         result=fun()+'hi'
#         return result
#     return method
#
# @decorator
# def greet():
#     return 'fazal'
#
# s=greet()
# print(s)


# for i in people:
#     if "name" in i:
#         print(i["name"])
#
# for i in people:
#     if i["age"] >32:
#         print(i["age"])
#
#
# f=[i for i in people if "name" in i and "age" in i and "location" not in i]
# print(f)
#

people = [
    {"name": "Alice", "age": 30, "location": "New York"},
    {"name": "Charlie", "age": 35, "location": "Chicago"},
    {"name": "Charlie", "age": 35},
    {"name": "Eve", "age": 32}
]

# f=[i for i in people if "location" not in i]
# print(f)

# for i in people:
#     if i["name"]=="Alice":
#         print(f"name is :{i['name']}")

# s=sorted(people,key=lambda x:x["age"])
# print(s)



# key="name"
# value=(a[key])
# print(f"key={key} and value={value}")
# print(a["name"])

# def decorator(fun):
#     def change(name):
#         result=fun(name)
#         return f"my name is {result}"
#     return change
#
# @decorator
# def greet(n):
#     return n
# s=greet('fazal')
# print(s)

# def decorator(fun):
#     def change(name):
#         result=fun(name)
#         return f"my name is {result}"
#     return change
#
# @decorator
# def greet(n):
#     return n
# s=greet('fazal')
# print(s)

# a={"name": "Alice", "age": 30, "location": "New York"}
#
# print(a["name"])
# # a["gender"]="female"
# # print(a)


# start=0
# end=len(s)-1
# while start<end:
#     s[start],s[end]=s[end],s[start]
#     start+=1
#     end-=1
#
# print(s)

# for i in range(len(s)):
#     for j in range(i+1,len(s)-1):
#         if s[i]==s[j]:
#             s.pop(j)
# print(s)
#
# for i in range(len(s)):
#     for j in range(i+1,len(s)-i-1):
#         if s[i]>s[j]:
#             s[i],s[j]=s[j],s[i]
#
# print(s[-2])
# arr=[1,2,3,4,5,6,3,4,6,2,1,7,8,9,16,10]
# largest=s_largest=arr[0]
# for num in arr:
#     if num>largest:
#         s_largest=largest
#         largest=num
#     elif num>s_largest and num!=largest:
#         s_largest=num
#
#
# print(s_largest)

# def decorator(fun):
#     def change():
#         result=fun()
#         return result.upper()
#     return change
# @decorator
# def greet():
#     return 'fazal'
#
# s=greet()
# print(s)

# class name:
#     def names(self):
#         s=10
#         print('parent')
#
# class name1(name):
#     def names1(self):
#         super().names()
#         print('child')
# s=name1()
# s.names1()

import abc
# from abc import ABC,abstractmethod
#
# class name(ABC):
#     def display(self):
#         print('abstract class')
# class name2(name):
#     def display(self):
#         super().display()
#         print('sub class')
#
# s=name2()
# s.display()

# import copy
# a=[1,2,[3,4]]
# shallow=copy.copy(a)
# shallow[2][0]=10
# print(a)
# print(shallow)
#
#
# import copy
# a=[1,2,[3,4]]
# deep=copy.deepcopy(a)
# deep[2][0]=10
# print(deep)
# print(a)
#
# s=lambda x:x*x
# print(s(10))

# s=(1,2,3,4,5)
# k=(6,7)
# # print(s+k)
# s=[1,2,3]
# b=[4,5]
# print(s+b)

# s=[1,2,3,4,5]
#
# def generator(s):
#     for i in s:
#         yield i
#
# s=generator(s)
# print(next(s))
# print(next(s))

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=i*f
#     return f
# s=fact(5)
# print(s)
