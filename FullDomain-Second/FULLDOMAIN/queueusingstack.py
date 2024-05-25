stack1=[]
stack2=[]
def push(a):
    stack1.append(a)
    print(stack1)

def pop():
    while stack1:
        stack2.append(stack1.pop())
    stack2.pop()

    while stack2:
        stack1.append(stack2.pop())
    print(stack1)

push(10)
push(20)
push(30)
push(40)
push(50)
pop()