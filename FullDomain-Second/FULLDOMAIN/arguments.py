# ............positional argument

def hello(a):
    print(a)
hello('hello')
# ............keyword argument

def hello(a,b):
    print(a+' '+b)

hello(b='s',a='fazal')

# ............default argument

def hello(a='hello'):
     print(a)

hello()

# ............variable length argument

def find_sum(*args):
    print(sum(args))

find_sum(1,2,3,4,5,6)

class find_sum:
    def __init__(self,*args):
        self.args=args

    def sums(self):
        s=sum(self.args)
        print(s)

s=find_sum(1,2,3,4,5,6,7,8,9,10)
s.sums()

class data:
    def __init__(self,**kwargs):
        self.kwargs=kwargs
    def datas(self):
        print(self.kwargs)

s=data(name='fazal',age='21',location='kochi')
s.datas()