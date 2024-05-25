# x=9
# l=lambda x:x*x
# print(l(x))

# list1=[1,2,3,4,5,6]
#
# tuple1=tuple(list1)
# print(tuple1)
# print(tuple1[1])
# t1=(1,2,3)
# a,b,c=t1
# print(a)
# c=tuple1+t1
# print(c)
#
# print(tuple1[1:3])

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
#
# print(fact(5))

# from mypackage import arithametic
# s=arithametic.square(200)
# print(s)

# list1=[1,2,3,4,5,6,7,8,9,10]
#
# s=iter(list1)
# print(next(s))
# print(next(s))
# print(next(s))

# d={"name":"fazal","age":21,"location":"kochi"}
#
# for i in d:
#     print(i)
#     print(d[i])

# print(f"key={'name'} and value={d['name']}")

# class name:
#     def home(self):
#         print('hello')
# class name2(name):
#     def home2(self):
#         super().home()
#         print('hai')
# s=name2()
# s.home2()
#
# s=100
# l=lambda x:x*x
# print(l(s))
#
# l=[1,2,3,4,5,6,7,8,9,10]
#
# s=list(x*x for x in l )
# print(s)
# s=list(x*x for x in l )

# def gen(n):
#     for i in range(n):
#         yield i
#
# s=gen(5)
# for i in range(5):
#     print(next(s))

# list1=[1,2,3,4,5,6,7,8,9,10]
#
# # l=list(map(lambda x:x*x,list1))
# # print(l)
#
# f=list(filter(lambda x:x%2==0,list1))
# print(f)


# people = [
#     {"name": "Alice", "age": 30, "location": "New York"},
#     {"name": "Charlie", "age": 35, "location": "Chicago"},
#     {"name": "Charlie", "age": 35},
#     {"name": "Eve", "age": 32}
# ]
# print(f"name is :{people[0]['name']}")
# f=sorted(people,key=lambda x:x["age"])
# print(f)
# for i in people:
#     if "location" not in i:
#         print(i)
#

# list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,3,1,7,15]

# a=[]
# for i in range(2,len(list1)+1):
#     s=0
#     for j in range(2,i):
#         if i%j==0:
#             s=1
#             break
#     if s==0:
#         a.append(i)
#
# print(a)
#
#

#...................................duplicate finding
# s=[]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]==list1[j] and list1[i] not in s:
#             list1[i]=0
#             s.append(list1[i])
# print(s)
# print(list1)

# l=[1,2,0,9,0,7,0,43,12]
#
# for i in range(len(l)):
#     if l[i]==0:
#         s=l.pop(i)
#         l.append(s)
#
#
# print(l)

# s='fazal'
# b=''
# for i in s:
#    b=i+b
# print(b)
#
# s={"name": "Alice", "age": 30, "location": "New York"}
#
# for i in s:
#     print(i)
#
# for i in s.values():
#     print(i)

#
# from packages import multiple
#
# s=multiple.multiple(10,10)
# print(s)

# x=10
# y=20
# r=x if  x>y else y
# print(r)


#
# k=iter(s)
# print(next(k))

# l=[x for x in s if x%2]
# print(l)
#
# k=[x*x for x in s]
# print(k)
#
# x=int(3.12)
# print(x)

# s='fazal'
# k=s[2:]
# print(k)

# s=[1,2,3,4,5,6,7,8,10]
# k=('fazal','faza','siva')
# s.extend(k)
# print(s)

# s[2]='fazal'
# print(s)
# s.insert(6,100)
# print(s)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# l=[i for i in fruits if 'a' in i]
# print(l)

# s={1,2,3,4,5}
# s.add(9)
# print(s)

# a=[1,2,3,4,5,6,7,8,10]
# for i in range(0, len(a), 3):
#     print(a[i])

# list1=[1,2,3,4,5,6,7,8,9]
#
# def reverse(lst,start,end):
#     while start<end:
#         lst[start],lst[end]=lst[end],lst[start]
#         start+=1
#         end-=1
#
# for i in range(0,len(list1),3):
#     reverse(list1,i,i+2)
#
# print(list1)

# i=0
# while i<6:
#     i+=1
#     if i==3:
#         continue
#     print(i)


# class animal:
#     def speak(self):
#         pass
# class dog(animal):
#       def speak(self):
#           print('woof')
# class cat(animal):
#     def speak(self):
#         print('meow')
#
# d=dog()
# c=cat()
# d.speak()
# c.speak()

# try:
#     print(x)
# except:
#     print('exception occured')
#
# def a(b,c):
#     print(b,c)
#
# a(c=9,b=50)

# a=(1,2,3,4)
# b=(5,6)
# print(a+b)

# a=10
# b=30
# t=a if a>b else b
# print(t)

# arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# odd=[]
# for i in arr:
#     if i%2==1:
#         odd.append(i)
# print(odd)
# l=odd[0]
# for i in range(1,len(odd)):
#     if odd[i]>l:
#         l=odd[i]
#
# print(l)

# s={"name": "Alice", "age": 30, "location": "New York"}

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
#
# for i in range(10):
#     print(fibonacci(i))

# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#     return a
#
# for i in range(10):
#     print(fibo(i))

# orginal=10
# copy1=orginal
# copy1=60
# print(orginal)

# orginal=[1,2,3]
# copy1=orginal
# copy1.append(4)
# print(orginal)

people = [
    {"name": "Alice", "age": 30, "location": "New York"},
    {"name": "Charlie", "age": 35, "location": "Chicago"},
    {"name": "Charlie", "age": 35},
    {"name": "Eve", "age": 32}
]
# print(people[0]["age"])
# f=[i for i in people if "location" not in i]
# print(f)


# f=sorted(people,key=lambda x:x["age"])
# print(f)
s={"name": "Alice", "age": 30, "location": "New York"}


# for i in s.keys():
#     print(i)
# k=s["name"]
# print(f"name={k}")
#
# l=list(map(lambda x:x*x,arr))
# print(l)
#
# s=[x*x for x in arr]
# print(s)
#
# f=list(filter(lambda x:x%2==0,range(1,20)))
# print(f)


# count=0
# a=[]
#
# for i in arr:
#     if i not in a:
#         count+=1
#         a.append(i)
# print(count)

# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)-1):
#         if arr[i]==arr[j]:
#             count+=1
#             a.append(arr[i])
#
# print(count)

# arr[0],arr[-1]=arr[-1],arr[0]
#
# print(arr)
#
# arr=[1,2,3,4,5,6]
# arr2=[12,34,45,65,67,4]

# def fun(arr,arr2):
#     for i in range(len(arr)-1):
#         for j in range(len(arr2)-1):
#             if arr[i]==arr2[j]:
#                 return True
#
# fun(arr,arr2)


# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)-1):
#         if arr[i]==arr[j]:
#             arr.pop(j)
#
# print(arr)

# def decorator(fun):
#     def change(name):
#         result=fun(name)
#         return f"my name is {result}"
#     return change
#
# @decorator
# def greet(n):
#     return n
#
# s=greet('fazal')
# print(s)

# class a:
#     def change(self):
#         print("kwargs")
# class b(a):
#     def hello(self):
#         super().change()
#         print('hello')
# s=b()
# s.hello()

# a=[1,2,3]
# b=a
# b[0]=10
# print(a)

# import copy
# a=[1,2,3]
# b=copy.deepcopy(a)
# b[0]=10
# print(a)

# import copy
# a=[1,2,3]
# b=copy.deepcopy(a)
# b[0]=10
# print(a)


# s=lambda a:a*a
# print(s(10))

# a=[1,2,3,4,5]
#
# def gen(a):
#     for i in a:
#         yield i
#
# s=gen(a)
# print(next(s))

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(fact(5))
#
# a,b=100,20
# print(a if a>b else b)
# a=[1,2,3,4,5]
# l=[x*x for x in a]
# print(l)
# m=list(map(lambda x:x*x,a))
# print(m)
#
# f=list(filter(lambda x:x%2==0,a))
# print(f)

# def fibo(n):
#     a,b=0,1
#     while a<n:
#         print(a)
#         a,b=b,a+b
#     print()
#
# fibo(10)

#.......................................inheritance
# class A:
#     def __init__(self,name):
#         self.name=name
#
# class B(A):
#     def speak(self):
#         return f"{self.name} says woof"
#
# s=B('dog')
# s=s.speak()
# print(s)

#.......................................abstracton

# from abc import ABC,abstractmethod
#
# class animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
# class dog(animal):
#     def speak(self):
#         print('dog says woof')
#
# s=dog()
# s.speak()
#
# people = [
#     {"name": "Alice", "age": 30, "location": "New York"},
#     {"name": "Charlie", "age": 35, "location": "Chicago"},
#     {"name": "Charlie", "age": 35},
#     {"name": "Eve", "age": 32}
# ]
#
# f={"name": "Charlie", "age": 35, "location": "Chicago"}
#
# for i in f:
#     print(i)
#
#
# f=sorted(people,key=lambda x:x["age"])
# print(f)

# a=[1,2,3,5,3,4,5,6,7,8,9,7,10,6]
# d={x:x*x for x in a}
# print(d)

# count=0
# for i in range(len(a)):
#     f=0
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             f=1
#             break
#     if f==1:
#         count+=1
#
# print(count)

# p=[]
# for i in a:
#     f=0
#     for j in range(2,i):
#         if i%j==0:
#             f=1
#             break
#     if f==0:
#         p.append(i)
# print(p)

# arr=[1,2,3,4,5,6,7,8,9,10]
# s=[1,2,3]
# arr.extend(s)
# print(arr)

# list=[]
# set=set()
# dict={}
# tuple1=()
#
# list.append(10)
# print(list)
#
# set.add(11)
# print(set)
#
# dict[1]=10
# print(dict)
#
# newtuple=tuple1+(100,)
# print(newtuple)

# s='fazal'
# b=''
# for i in s:
#     b=i+b
# print(b)

a=[1,2,3,4,5,6,7,8,9,10,11]


# def fibo(n):
#     a,b=0,1
#     while a<n:
#         print(a)
#         a,b=b+a,a
# fibo(10)

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(fact(5))


# start=0
# end=len(a)-1
# while start<end:
#     a[start],a[end]=a[end],a[start]
#     start+=1
#     end-=1
#
# print(a)


# b=[]
# count=0
# for i in range(len(a)):
#     f=0
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             f=1
#     if f==0:
#         count+=1
#
# print(b)
# print(count)


# p=[]
# for i in a:
#     f=0
#     for j in range(2,i):
#         if i%j==0:
#             f=1
#             break
#     if f==0 and i !=1:
#         p.append(i)
#
# print(p)

#.....................super keyword
# class parent:
#     def show(self):
#         print('parent class')
#
# class child(parent):
#     def show(self):
#         super().show()
#         print('child class')
#
# obj=child()
# obj.show()

# import copy
# a=[1,2,3]
# b=copy.deepcopy(a)
# b[0]=20
# print(a)

# l=lambda x:x*x
# print(l(50))

# t=()
# t=t+(10,)
# print(t)
#
# a=[1,2,3,4,5,6,7,8,9,10,11]
#
# l=[i for i in a if i%2==0]
# # l=[i*i for i in a]
# print(l)

# def gen(a):
#     for i in a:
#         yield i
# s=gen(a)
# print(next(s))

# s=iter(a)
# print(next(s))
# print(next(s))

# from mypackage1 import sum2
#
# s=sum2.add(10,20)
# print(s)

# a=10
# b=20
#
# s=a if a>b else b
# print(s)

# t=(1,2,4)
# a,b,c=t
# print(a)


# list1 = [1, 2, 3]
# list2 = list1
# list2[0]=10
# print(list1)

# import copy
# list1 = [1, 2, 3]
# list2 = copy.deepcopy(list1)
# list2[0]=10
# print(list1)

# i=1
# while i<11:
#     if i==3:
#         i+=1
#         continue
#     print(i)
#     i+=1

# list1=[1,2,3,4,5]
# m=list(map(lambda x:x*x,list1))
# print(m)
#
# f=list(filter(lambda x:x%2==0,list1))
# print(f)
#
# dict={x:x*x for x in list1}
# print(dict)

# try:
#     file=open(r'C:\Users\sarat\Downloads\Postgres.txt','r')
#     content=file.read()
#     print(content)
# except:
#     print('flie not found')
#
# finally:
#     file.close()
#     print('file closed')
#
#

# try:
#    f=open('tex.txt','r')
# except FileNotFoundError as e:
#     print(e)

# for i in range(5):
#     for j in range(5-i):
#         print('*',end=' ')
#
#     print()
#
# people = [
#     {"name": "Alice", "age": 30, "location": "New York"},
#     {"name": "Charlie", "age": 35, "location": "Chicago"},
#     {"name": "Charlie", "age": 35},
#     {"name": "Eve", "age": 32}
# ]
#
# g=[i for i in people if "location" in i]
# print(g)
#
# f={"name": "Charlie", "age": 35, "location": "Chicago"}
#
# print(f"name={people[0]['name']}")

# print(people[0]["name"])
# for i in people[0]:
#     print(i)
#     print(people[0][i])
#
# s=sorted(people,key=lambda x:x["age"])
# print(s)
# for i in people:
#     if "location" in i:
#         print(i)

# l=[]
# t=()
# s=set()
# d={}
# l.append(10)
# l[0]=11
# print(l)
# t=t+(10,)
# print(t)
#
# s.add(10)
# print(s)
#
#
# d[10]=50
# d.update({10:100})
# d.pop(10)
# print(d)

# def decorator(fun):
#     def name(n):
#         result=fun(n)
#         return f"my name is {result}"
#     return name
# @decorator
# def greet(n):
#     return n
# print(greet('fazal'))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def validate_bst(root):
#
#     if not root:
#         return True
#
#     # Check if the left subtree is a BST.
#     left_valid = validate_bst(root.left)
#     if not left_valid:
#         return False
#
#     # Check if the right subtree is a BST.
#     right_valid = validate_bst(root.right)
#     if not right_valid:
#         return False
#
#     # Check if the current node violates the BST property.
#     if root.left and root.left.data >= root.data:
#         return False
#     if root.right and root.right.data <= root.data:
#         return False
#
#     # The tree is a BST.
#     return True
#
# root = Node(5)
# root.left = Node(3)
# root.right = Node(7)
#
# is_bst = validate_bst(root)
#
# print(is_bst)




# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
#
#     if node is None:
#         return True
#
#     if node.value < min_val or node.value > max_val:
#         return False
#
#     return is_valid_bst(node.left, min_val, node.value) and is_valid_bst(node.right, node.value, max_val)
#
# # Create a valid BST
# root = Node(5)
# root.left = Node(3)
# root.right = Node(7)
#
# # Check if the tree is a valid BST
# print(is_valid_bst(root))
#


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# def validate_bst(node, min_val=float('-inf'), max_val=float('inf')):
#     if node is None:
#         return True
#
#     if node.value < min_val or node.value > max_val:
#         return False
#
#     return validate_bst(node.left, min_val, node.value) and validate_bst(node.right, node.value, max_val)
#
#
# root = Node(5)
# root.left = Node(2)
# root.right = Node(1)
# print(validate_bst(root))
#

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def tree_height(root):
#     if root is None:
#         return 0
#     else:
#         left_height = tree_height(root.left)
#         right_height = tree_height(root.right)
#         return 1 + max(left_height, right_height)
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# # Calculate the height of the tree
# height = tree_height(root)
# print("Height of the tree:", height)

##################################################################################################################

# setting a response code for a response
# def my_view(request):
#     response = HttpResponse('page not found', status = 404)
#     return response

# setting a default value to templates

# {{variable | default : 'default value'}}

from FULLDOMAIN.DS3 import sums

s = sums.find_sum(10, 20)
print(s)

