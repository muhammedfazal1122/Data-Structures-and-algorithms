
# .........................variable length arguments

def sum1(*args):
    return sum(args)

k=sum1(1,2,3,4,5)
print(k)


def sum1(*args):
    return sum(args)

print(sum1(1,2,4,5,6,6))

def concatinate(*args):
    return ' '.join(args)

s=concatinate('hello','world')
print(s,"ssssssssssss")

#....................................................kwargs...................

def user(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

user(name='fazal',age=21,city='alappy')


