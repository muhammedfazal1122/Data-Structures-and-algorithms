class Stack:
    def __init__(self):
        self.que1 = []
        self.que2 = []

    def push(self, x):
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.pop(0))
        self.que1, self.que2 = self.que2, self.que1

    def pop(self):
        if self.que1 is None:
            return None
        return self.que1.pop(0)

    def top(self):
        if self.que1 is None:
            return None

        return self.que1[0]

    def display(self):
        print(self.que1)
        
obj = Stack()
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(8)
obj.display()

print('top=', obj.top())
print('popped elt=', obj.pop())
print('top=', obj.top())
print('popped elt=', obj.pop())

print(obj.top())
print(obj.top())
