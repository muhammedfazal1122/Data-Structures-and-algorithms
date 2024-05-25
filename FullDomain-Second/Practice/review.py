 
# # data type
#
# #list :-
# list = [1, "amal", 1.5, True ]
# print(list)

# #tuple:-
# tuple1 =("parrot","eagle",("lion","tiger"))
#
# print(tuple1[2][1])
# print(tuple1[2])
#
# #dict:-
# dict = {"name": "siva","age": 24, "canVote": True}
#
# #typecast
# #explicit:-
# a = "1"
# b = "2"
# print(int(a)+int(b))
# print(a+b)

# implicit
# a = 1
# b = 3.78
# print(a+b)
#
# #STRING :-
# name = "rajarajewsara venkita"
# for i in name:
#     print(i)
#
# #SLICING


# name="Muhammed FAzaL "
# print(name[2:-7])
# name = "Amal Siva"
# print(name[-4:-1])
# # IF ELSE/ELIF/NESTED IF ELSE
# IF ELSE:-
# a = float(input('enter the price'))
# budget = 200
# if a < budget:
#     print('buy')
# else:
#     print('dont buy')
# #ELIF
# num = float(input('enter the number : '))
# if num<0:
#     print('num is neg')
# elif num>0:
#     if num>0 and num<=10:
#         print('num greater than 0 & 10')
#     elif num>11 and num<=20:
#         print('num is bitween 10 & 20')
#     else:
#         print('num is positive and greater than 20')
#
# #Exersice
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = int(time.strftime('%M'))
# if timestamp >=29:
#     print('gd eveng')
# else:
#     print('not the crct time')
#
# #Match case
# x = int(input('enter num'))
# match x:
#     case 0:
#         print('hi')
#     case 1:
#         print('hello')
#     case 2:
#         print('wht')
#     case _:
#         print('tku')
#
# #LOOP
# For Loop
# for i in range(20):
#     print(i)
# While loop increment
# i = 0
# while (i<=10):
#     print(i)
#     i = i+ 1
#
# DO WHILE EMULATION1
# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break


# DO WHILE EMULATION2
# i = 100
# while True:
#   print(i)
#   i = i - 1
#   if(i == 0):
#     break
#
# #FUNCTION1
# def isDivision(a,b):
#   div = a/b
#   print('answer is :',div)
#
# a = int(input('enter 1st num'))
# b = int(input('enter 2nd num'))
# isDivision(a,b)
#
# REQUIRED ARGUMENT
# def sum(a,b = "joe ",c ="chad"):
#   print(a+b+c)
#
# sum("w ","ricky")
#
# ARBITARY ARGUMENT
# def average(*numbers):
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   print('average : ',(sum/len(numbers)))
#
# average(2,2,2,2,2,2)
#
# #LISTS
# Reversal of list
# list1 = [1,2,33,4,5,7,6,4,8,9]
# a = len(list1)
# print(a)
# b = list1[-1:-11:-1]
# print(b)
#
# list comprehension
# list1 = [i*i for i  in range(10)]
# print(list1)
#
# methods
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b =
# a[0] = 0
# print(a)
# print(b)
#
#RECURSION
# Factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

# Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    else:
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-1] + seq[i-2])
        return seq

print(fibonacci(10))
#
# SET
# siva = {1, True, "hi", 3.454, 1, 1}
# # for i in siva:
# print(siva)
#
# Set methods
# union
# cities = {'blu','coa','tov','emrae'}
# cities1 = {'coa','mil','emrae','gil'}
# city = cities.union(cities1)
# print(city)
#
# intersection
# cities = {'blu','coa','tov','emrae'}
# cities1 = {'coa','mil','emrae','gil'}
# city = cities.intersection(cities1)
# print(city)
#
# Difference
# cities = {'blu','coa','tov','emrae'}
# cities1 = {'coa','mil','emrae','gil'}
# city = cities.difference(cities1)
# print(city)
#
# Symmetrical difference
# cities = {'blu','coa','tov','emrae'}
# cities1 = {'coa','mil','emrae','gil'}
# city = cities.symmetric_difference(cities1)
# print(city)
#
# DICTIONARY
# id = {363 : 'blu', 777 : "siva", 676 : "oreo", 845 : "bane"}
# print(id[777])
#
# #EXCEPTION HANDLING
# try:
#     num = int(input('enter a value'))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("input value is not an integer")
# except IndexError:
#     print("Index out of bound")
#
# #Finally
# def func():
#     try:
#         l = [100,235,450,112,874,654,224,777,512]
#         i = int(input('enter the value'))
#         print(l[i])
#         return 'program executed 0'
#     except:
#         print('some error occured')
#     # finally:
#     #     print('I am always executed')
#
# print(func())
#
# #Custom Error
# a = int(input('enter a num bitween 5 and 9'))
# if (a<5 or a>9):
#     raise ValueError("ERROR!! Value is not bitween 5 & 9")
#
# #SHORT HAND IF ELSE
#
# a = 300
# b = 200
# print("A") if a > b else print("=") if a == b else print("B")
# c = 9 if a>b else 0
# print(c)
# #ENUMERATE FUNCTION
# names = ['amal','siva','mangadath','pullani','thuravoor','angamaly','kochi']
# for index, name in enumerate(names,start=1):
#     print(index,name)
#     if index == index:
#         print(" ")
#
# #LAMBDA FUNCTION:
# Passed as an argument
#
# def multi(fx, a,b):
#     return fx(a,b)
#
# mul = lambda x,y: x*y
#
# print(multi(mul,6,5))
# # print(multi(lambda x,y: x*y,6,5))
#
# #MAP-FILTER-REDUCE
# MAP
# def double(b):
#     return b*2
# a = [1,2,3,4,5]
# newl = list(map(double,a))
# print(newl)
#
# #FILTER
#
# def filter_fun(c):
#     return c>3
# a = [1,2,3,4,5]
#
# newnewl = list(filter(filter_fun,a))
# print(newnewl)
#
# #REDUCE
# from functools import reduce
# number = [1,2,3,4,5]
# def mysum(a,b):
#     return a+b
#
# l = reduce(mysum,number)
# print(l)
#
# def count_occurrences(values):
#     occurrence_count = {}
#     for value in values:
#         if value in occurrence_count:
#             occurrence_count[value] += 1
#         else:
#             occurrence_count[value] = 1
#     return occurrence_count
# my_list = [1, 2, 3, 2, 1, 3, 4, 5, 4, 2, 2, 3]
#
# result = count_occurrences(my_list)
# print(result)
#
# #OOPS
# class Car:
#     def __init__(self,make, model):
#         self.make = make
#         self.model = model
#         print(self.make,self.model)
#
#     def start_engine(self):
#         print("Engine started.")
#
# my_car = Car("Toyota", "Corolla")
# my_car = Car("Ferrari","la ferrari")
# my_car = Car("Keionegeggs","Gemera")
# my_car.start_engine()
#
# class A:
#     def dec(self, func):
#         def wrapper(x):
#             print('hello')
#             return func(x)
#         return wrapper
#
#     def multi(self, x):
#         return x * x
#
# class B(A):
#     def __init__(self, name):
#         self.name = name
#
# c = B(10)
# a = A()
#
# @a.dec  # Instantiate A and apply the decorator
# def y(x):
#     print('blu')
#
# y(10)
#
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# closure_func = outer_function(10)
# result = closure_func(5)
# print(result)
# x = int(input('num'))
# def seq(x):
#     a = [0,1]
#     for i in range(2, x):
#         a.append(a[i-1]+a[i-2])
#     return a
#
# print(seq(10))
#
# a = "siva"
# b = a[-1:5:-]
# print(b)
#
# #SPLIT
# str = "hello my world"
# str1 = str[7:]
# print(str1)
# st= str.split(" ")
# print(st[-1])
#
# def dec(func):
#     def wrapper(x, y):
#         div = x / y
#         if div < 10:
#             print(div)
#             print('less than 10')
#         else:
#             print(div)
#             print('more than or equal to 10')
#         return func(x, y)
#     return wrapper
#
#
# @dec
# def num(x, y):
#     pass
#
# num(20, 5)
#
# #GENERATOR
# def gen (x):
#     for i in range(0,11):
#         multi = i * x
#         yield multi
# res = gen(5)
# for i in res:
#     print(i)
#
# marks = [("blu",'10'),("siva",'15'),("luk",'12')]
# marks.sort(key = lambda x:x[1])
# print(marks)
#
# #map
#
# def sqr(x):
#     return x*x
#
# list1 = [1,2,3,4,5,6]
# mapped_list = list(map(sqr,list1))
# print(mapped_list)
#
# list1 = [1,-2,-5,4,5]
# print(list(map(abs,list1)))
#
# def word_counter(words):
#     new_count = {}
#     for word in words:
#         if word in new_count:
#             new_count[word] += 1
#         else:
#             new_count[word] = 1
#     return new_count
#
# list1 = "banana"
# result = word_counter(list1)
# print(result)
#
# def pnum(nums):
#    return True if nums>0 else  False
#
# nums = [ 1,-5,-8,10,54,-65,18]
# print(list(filter(pnum, nums)))
#
#
# class Account:
#    def __init__(self, account_name,account_balance):
#       self.account_name = account_name
#       self.account_balance = account_balance
#
#    def withdraw(self,amount):
#       if self.account_balance - amount < 0:
#          print("Please check your balance. Your balance is too low")
#       else :
#          self.account_balance = self.account_balance - amount
#          print(f"You have withdrawn {amount} from your account")
#
#    def display(self):
#       print(f"Your balance is {self.account_balance}")
#
# acc1 = Account("Siva",500000)
# acc2 = Account("amal",155002)
# acc1.withdraw(50000)
# acc1.display()
# #PALINDROME
# str1 = "MALAYAkM"
# l = len(str1)-1
# for i  in range(l//2):
#     if str1[i] != str1[l-i]:
#         print("not pali")
#         break
# else:
#     print("palindrome")
#
# num = int(input('enter a num'))
# n1, n2 = 0, 1
# sum = 0
# if num <= 0:
#     print('enter value larger than 0')
# else :
#     for i in range(num):
#         print(sum,end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
#
#
# def fibonnaci(n):
#     if n <= 0:
#         print('enter value greater than 0')
#     else :
#         seq = [0, 1]
#         for i in range(2,n):
#             seq.append(seq[i-1] + seq[i-2])
#         return seq
#
# print(fibonnaci(10))
#
#
# i= 0
# num = int(input('num:'))
# def fibbonacci(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     return fibbonacci(num-1) + fibbonacci(num-2)
#
# for i in range(0,num):
#     print(fibbonacci(i),end=" ")
#
#
# #FIND IF ITS PRIME
# num = int(input('enter the number'))
# for i in range(2, int(num**0.5)+1):
#     if num % i == 0:
#         print(num,"not a prime")
#         break
# else:
#     print(num,"is prime")
#
# #PRIME SERIES
# strt = int(input('enter the strt value'))
# end = int(input('enter the end value'))
# for i in range(strt,end):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else :
#         print(i,end=" ")
#
# def is_prime(num):
#     for i in range(2,num-1):
#         if num % i == 0:
#             print('not prime')
#             break
#     else:
#         print('is prime')
#
# is_prime(17)
#
# def is_Palindrome(word):
#     l = len(word)-1
#     for i in range(0,l//2):
#         if word[i] != word[l-i]:
#             print('not a palindrome')
#             break
#     else:
#         print('Is a palindrome')
#
# word = str(input('enter a word'))
#
# is_Palindrome(word)
#
#
# # FACTORIAL
# def fact(num):
#     if num <=1:
#         return 1
#     else:
#         return num * fact(num-1)
# num = int(input('enter a num'))
# print(fact(num))
#
# #DECORATOR
#
# def deco(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
#
# def greet():
#     print("running")
#
# deco(greet)()
#
# ##############################
#
# def dec(func):
#     def wrapper(*args,**kwargs):
#         print('start')
#         val = func(*args,**kwargs)
#         print(val)
#         if val < 1:
#             print(val,'less than 1')
#         else:
#             print(val,'value is more than 1')
#         print('ended')
#     return wrapper
# @dec
# def dvs(x,y):
#     return x / y
# dvs(100,5)
#
# ##################################
# def gen():
#     n = 1
#     print('1st one')
#     yield n
#     n+=1
#     print('2nd one')
#     yield n
#     n+=1
#     print('3rd one')
#     yield n
#
# a  = gen()
# for i in a:
#     print(i)
# ##########################################
# li = [1,2,3,4,5,6]
# lists = [x**2 for x in li]
# generator = (x**2 for x in li)
# print(lists)
# for i in generator:
#     print(i, end=" ")
#
# ##############################
# #infite loop
#
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
# for item in all_even():
#     print(item)
#
# ############################
# #fibonacci using generator
#
# def fibonacci(num):
#     x,y = 0,1
#     for i in range(0,num):
#         x , y =  y, x+y
#         yield x
#
# fib = fibonacci(10)
# for i in fib:
#     print(i, end=" ")
#
# a = [1,2,3,4,5,6]
# list1 = [x/2 for x in a]
# print(list1)
# #############################################
# lst = [1,2,3,4,5]
# m= list(map(lambda x : x**3,lst))
# print(m)
# ############################
# i=0
# num = int(input('num : '))
# def fib(num):
#     if num == 1 or num == 0:
#         return num
#     else:
#         return num*fib(num-1)
#
#
# print(fib(num))
# def gen (num):
#     for i in range(0, num):
#         yield i
# a = gen(10)
# for i in a:
#     print(i,end=" ")
# ###################################
#
# class Vehicle:
#     def __init__(self, brand,model):
#         self.brand = brand
#         self.model = model
#
#     def engine(self):
#         print('Engine  strated')
#
#     def display(self):
#         print(f"your vehicle is {self.brand} and model is {self.model}")
#
# class Car(Vehicle):
#     def engine(self):
#         print("engine rev")
#
# car1 = Car("Honda","R34")
# bike = Vehicle("bmw","100RR")
# car1.display()
# car1.engine()
# bike.engine()
#
# class Overload:
#     def add(self,*args):
#         sum = 0
#         for i in args:
#             sum = sum + i
#         return sum
#
# a= Overload()
# print(a.add(10,10,10,10,10,49.9999999999))
# ################################################
# def dec (func):
#     def wrapper(*args):
#         list1 = []
#         for i in args:
#             list1.append(i)
#         print(list1)
#     return wrapper
# @dec
# def push(*args):
#     return push
#
# push(10,20,30,40,50,60)
# ##################################################
list1 = [1,2,3,4,5,6,7,8,9,10]
def sq(list):
    return list**2

list2 = list(map(sq,list1))
print(list2)
       



# ##################################################
# class A:
#     def method(self):
#         print("A's method")
#
# class B(A):
#     def method(self):
#         print("B's method")
#
# class C(A):
#     def method(self):
#         print("C's method")
#
# class D(C,B):
#     pass
#
# obj = D()
# obj.method()
#
# # Output: B's method
