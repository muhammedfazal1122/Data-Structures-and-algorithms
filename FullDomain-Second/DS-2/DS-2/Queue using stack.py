class quyeueUsingStack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def add(self,value):
        self.stack1.append(value)
        # print(self.stack1)





    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def desply(self):
        print(self.stack2)


queue=quyeueUsingStack()
queue.add(2)
queue.add(411)
queue.add(343)
queue.add(66)
queue.add(33)
queue.add(343)

queue.desply()  