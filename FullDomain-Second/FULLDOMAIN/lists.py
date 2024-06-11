# print(a)
# print(a[1])
# a.append(11)
# print(a)
# a.insert(0,0)
# print(a)
# a.pop()
# print(a)
# a.reverse()
# print(a)

# b=[]
# for i in range(len(a)):
#    b.append(a.pop())
# print(b)
# #
# b=[x*x for x in a]
# print(b)
# c=[x for x in a if x%2==0]
# print(c)
# a=[1,2,3,4,5,6,7,8,9,10]

# b=[x for x in range(1,30) if x%3==0]
# print(b)


# a=('apple','banana','cherry','orange')

# b,c,d,e=a

# print(b)
# print(c)
# print(d)
# print(e)

# ........................................dictionary comprehension...................

# dict={x:x*x for x in range(1,11)}

# print(dict)

# print(dict.keys())


# ..........................................................Lambda functions.....................................

# a=[1,2,3,4,5,6,7,8,9,10]

# x= lambda a:a*a
# print(x(5))


# .................................................Map...........................................................

# a=[1,2,3,4,5,6,7,8,9,10]
# l=list(map(lambda x:x*x,a))
# print(l)

# s=list(map(lambda a:a%2==0,a))

# print(s)

# s=list(filter(lambda x:x%2==0,a))
# print(s)
# s=list(filter(lambda k:k%2==1,a))
# print(s)

# .............................................INHERITANCE.......................................................

# class animal:
#     def __init__(self,behave):
#         self.behave=behave

#     def nature(self):
#         pass

# class dog(animal):
#     def dog(self):
#         print(f'dog have the behaviour of {self.behave}')

# s=dog('barking')
# s.dog()
# ...............................................

# a={'a':0,'e':0,'i':0,'o':0,'u':0}

# print(a.items())



# Generator function
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# # Using the generator
# gen = simple_generator()
# for value in gen:
#     print(value)


# def fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# g=fibo()
# for i in range(10):
#      print(next(g))

# #################################..................decorator...........................................

# def dec(fun):
#     def message():
#         print('function start')
#         result=fun()
#         print('function ends')
#         return result
#     return message

# @dec
# def greet():
#     print('hello')

# greet()

# def upper(fun):
#     def message():
#         result=fun()
#         return result.upper()
#     return message
# @upper
# def greet():
#     return 'hello world'

# s = greet()
# print(s)


# def data(fun):
#     def change():
#         result=fun()
#         return str(result)
#     return change

# @data
# def add():
#     return 5+3

# s=add()
# print(type(s))

# def count():
#     s='hello'
#     count={}
#     for i in s:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     return count

# s=count()3
# print(s)


# s = "fazal"
# m = ""

# for i in s:
#     m = i + m

# print("Reversed string is:", m)

# ..................................................

# def elementsum(arr):
#     while len(arr)>1:
#         firstsum=arr[0]+arr[1]
#         sums.append(firstsum)

#         if len(arr)>=2:
#             lastsum=arr[-1]+arr[-2]
#             sums.append(lastsum)

#         arr=arr[2:-2]

#     if len(arr)==1:
#         return arr[0]

#     return sums


# arr=[1,2,3,4,5,6,7,8,9]
# sums=[]
# s=elementsum(arr)
# sums.append(s)
# print(sums)


# s=[0]*11
# i=0
# j=0

# while i <= 10:
#     s[i] = i
#     i += 1

# print(s)

# a=[1,2,1,3,4,5,4,6,7,7]
# d={}
# s=[]
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value>1:
#         s.append(key)

# print(s)

# s=[]
# a=[1,2,1,3,4,5,4,6,7,7]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j] and a[i] not in s:
#             s.append(a[i])

# print(s)


# a=[1,2,3,4,5,6,7,8,9]
# start=0
# end=len(a)-1
# while start<end:
#     a[start],a[end]=a[end],a[start]
#     start+=1
#     end-=1

# print(a)


# s='fazal'
# l=''
# for i in s:
#     l=i+l

# print(l)

# a=[1,6,34,2,658,1,34,9]
# start=0
# end=len(a)-1
# while start<end:
#     a[start],a[end]=a[end],a[start]
#     start+=1
#     end-=1

# print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# o=[]
# for i in range(len(a)):
#     if i%2==1:
#         o.append(i)
# m=o[0]
# print(o)
# for i in range(1,len(o)):
#     if o[i]>m:
#         m=o[i]

# print(o[i])

# a=[1,2,3,4,5,6,7,8,9,10]

# i=iter(a)
# print(next(i))
# print(next(i))
# print(next(i))

# def num(n):
#     for i in range(n):
#         yield i

# s=num(10)
# print(next(s))
# print(next(s))


# def up(fun):
#     def change():
#         result=fun().upper()
#         return result
#     return change

# @up
# def name():
#     return 'fazal'
# print(name())

# s=lambda x:x*10
# print(s(5))

# a=[1,2,3,4,5,6,7,8,9,10]
# l=list(map(lambda x:x*x,a))
# print(l)


# l=list(filter(lambda x:x%2==0,a))
# print(l)

# a=[1,2,3,4,5,65,6,7,8,8]
# d={x:x*2 for x in a}
# print(d)
# def sum(n):
#     for i in range(n):
#         yield i  

# s=sum(10)
# print(next(s))
# print(next(s))
# print(next(s))
# for i in range(len(a)):
#     min=i
#     for j in range(i+1,len(a)):
#         if a[j]<a[min]:
#             min=j
#     a[i],a[min]=a[min],a[i]

# print(a)

# for i in range(1,len(a)):
#     c=a[i]
#     p=i
#     while c>a[p-1] and p>0:
#         a[p]=a[p-1]
#         p=p-1
#     a[p]=c

# print(a)