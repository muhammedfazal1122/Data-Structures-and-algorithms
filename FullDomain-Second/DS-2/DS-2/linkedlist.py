class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class list1:
    def __init__(self):
        self.head=None

    def add(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.ref=self.head
            self.head=newnode

    def addafter(self,data,x):
        n=self.head
        newnode=node(data)
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.ref

        if n is None:
            print('data not found')
        else:
            newnode.ref=n.ref 
            n.ref=newnode

    def addbefore(self,data,x):
        n=self.head
        newnode=node(data)
        while n is not None:
            if x==n.ref.data:
                break
            else:
                n=n.ref
        if n is None:
            print('data not found')
        else:
            newnode.ref=n.ref
            n.ref=newnode

    def display(self):
        n=self.head
        while n is not None:
            print(n.data,'-->',end='')
            n=n.ref


    def mid(self):
        n=self.head
        mid=self.head
        while n.ref is not None:
            prev=n
            mid=mid.ref
            n=n.ref.ref
        print('mid is ',mid.data)

    def delmid(self):
        n = self.head
        mid = self.head
        while n.ref is not None:
            prev = mid
            mid = mid.ref
            n = n.ref.ref
        prev.ref=prev.ref.ref



s=list1()
s.add(100)
s.add(200)
s.add(300)
s.addafter(500,200)
s.addbefore(600,100)
s.mid()
s.delmid()
s.display()

class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class list1:
    def __init__(self):
        self.head=None

    def add(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.ref=self.head
            self.head=newnode

    def display(self):
        n=self.head
        while n is not None:
            print(n.data,'-->',end='')
            n=n.ref

    def list1(self):
        s=[]
        current = self.head
        while current:
            s.append(current.data)
            current = current.ref
        s.reverse()
        for i in range(len(s)):
            f=0
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    f=1
                    break
            if f==1:
                print('the last duplicate value is', s[i])
                break

s=list1()
s.add(10)
s.add(20)
s.add(30)
s.add(10)
s.add(50)
s.add(20)
s.add(80)
s.display()
print()
s.list1()

class a:
    def hello(self):
        print('hello how')

class b(a):
    def hai(self):
        super().hello()
        print('hello')

k=b()
k.hai()