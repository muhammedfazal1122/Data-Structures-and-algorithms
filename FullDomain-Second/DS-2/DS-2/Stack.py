stack=[]
def add():
    element = (input('enter elemnt:'))
    added = stack.append(element)
    print('added elt:', added)
    print(stack)

def remove():
    if not stack:
        print('Stack Underflow')
    else:
        deleted=stack.pop()
        print('rmeoved elt is',deleted)
        print(stack)
def disp():
    print(stack)


temp_stack=[]
def delete_middle():
   mid=len(stack)//2
   for i in range(mid):
       temp_stack.append(stack.pop())
   stack.pop()
   for i in range(mid):
       stack.append(temp_stack.pop())
   print(stack)

def reverseStack(stack):
    temp_stack=[]
    while stack:
        temp_stack.append(stack.pop())
    print(temp_stack)

while True:
    print('1.push\n2.pop\n3.display\n4.exit\n5.delete mid\n6.revese\n')
    c=int(input('enter a choice:'))
    if c==1:
        add()
    elif c==2:
        remove()
    elif c==3:
        disp()
    elif c==4:
        break
    elif c==5:
        delete_middle()
    elif c==6:
        reverseStack(stack)
    else:
        print('enter valid input')
