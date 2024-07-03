
def decorator(fun):
    def datatype(*args):
        result=type(fun(*args))
        return result
    return datatype

@decorator
def sum1(a,b):
    return a+b

s=sum1(10,15)
print(s)

def decorator(fun):
    def upper1():
        result=fun().upper()
        return result
    return upper1

@decorator
def greet():
    return 'fazal'

s=greet()
print(s)


def decorator(fun):
    def change(name):
        result=fun(name)
        return f"my name is {result}"
    return change
@decorator
def name(n):
    return n

s=name('fazal')
print(s)


def decorator(fun):
    def caps(name):
        result=fun(name).upper()
        return result
    return caps
@decorator
def name(n):
    return n

s=name('fazal')
print(s)

def decorator(fun):
    def wrapper():
        res = fun().upper()
        return res
    return wrapper
    
@decorator
def greettting():
    return "hello fazzzalll"


print(greettting())




 
