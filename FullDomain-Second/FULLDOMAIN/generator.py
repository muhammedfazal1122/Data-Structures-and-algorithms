def num():
    n=0
    while True:
        yield n
        n+=1

s=num()

for i in range(10):
    print(next(s))

def cube(n):
    for i in range(1,n+1):
        yield i**3

s=cube(10)
for i in range(10):
    print(next(s))



def prime(n):
    for i in range(n):
        s = 0
        for j in range(2, i):
            if i % j == 0:
                s = 1
                break

        if s == 0:
            print('prime number is:', i)

prime(10)


def prime(n):
    for i in range(2,n):
        s=0
        for j in range(2,i):
            if i%j==0:
                s=1
                break

        if s==0:
            yield i

s=prime(15)

for k in range(5):
    print(next(s))


def fibo():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b
s=fibo()
for i in range(10):
    print(next(s))


# without yield

def fibo(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b

print(fibo(10))




def gennrator():
    n = 1
    while n <= 10 :
        sq = n*n
        yield sq
        n +=1

obj = gennrator()

for i in obj:
    print(i)


