queue=[]
queue2=[]
def add():
    value=int(input("enter the value"))
    queue.append(value)
    print(queue)

def remove():
    if not queue:
        print("there is no value to delete")
    else:
        queue.pop(0)
        print(queue)
def display():
    print(queue)

def mid_element():
    i=0
    mid=len(queue)//2
    while i<mid:
        queue2.append(queue.pop(mid))
        print(queue2)




while True:
    choice=input("enter 1 to 3:")
    if choice=="1":
        add()
    elif choice=="2":
        remove()
    elif choice=="3":
        display()
    elif choice=="5":
        mid_element()
    else:
        print("invalid choice")

