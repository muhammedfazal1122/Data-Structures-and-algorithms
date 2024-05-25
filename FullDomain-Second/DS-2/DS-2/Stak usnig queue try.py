class stackUsingQueue():
    def __init__(self):
        self.queue1=[]
        self.queue2=[]


    def push(self,value):
        self.queue2.append(value)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        self.queue2,self.queue1=self.queue1,self.queue2

    def remove(self):
        self.queue1.pop(0)

    def top(self):
        if not self.queue1 :
            print("there is no value")
        return self.queue1[0]

stack=stackUsingQueue()
stack.push(1)
print(stack.top())

stack.push(12)
print(stack.top())


stack.push(13)
print(stack.top())

stack.push(14)
print(stack.top())

stack.push(15)
print(stack.top())

stack.remove()
print(stack.top())
stack.remove()
print(stack.top())