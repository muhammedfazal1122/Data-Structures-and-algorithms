class Stack:
    def __init__(self):
        self.stack = []
        self.temp_stack = []
        self.n = int(input('Enter the number of elements:'))

    def add(self):
        if len(self.stack) == self.n:
            print('Stack Overflow')
        else:
            element = input('Enter element:')
            self.stack.append(element)
            print('Added element:', element)
            print(self.stack)

    def remove(self):
        if not self.stack:
            print('Stack Underflow')
        else:
            deleted = self.stack.pop(0)
            print('Removed element:', deleted)
            print(self.stack)

    def disp(self):
        print(self.stack)

    def delete_middle(self):
        mid = len(self.stack) // 2
        for i in range(mid):
            self.temp_stack.append(self.stack.pop())
        self.stack.pop()
        for i in range(mid):
            self.stack.append(self.temp_stack.pop())
        print(self.stack)

    def reverseStack(self):
        while self.stack:
            self.temp_stack.append(self.stack.pop())
        print(self.temp_stack)

if __name__ == "__main__":
    stack_obj = Stack()
    while True:
        print('1. Push\n2. Pop\n3. Display\n4. Exit\n5. Delete middle\n6. Reverse\n')
        choice = int(input('Enter your choice:'))
        if choice == 1:
            stack_obj.add()
        elif choice == 2:
            stack_obj.remove()
        elif choice == 3:
            stack_obj.disp()
        elif choice == 4:
            break
        elif choice == 5:
            stack_obj.delete_middle()
        elif choice == 6:
            stack_obj.reverseStack()
        else:
            print('Enter a valid input')
