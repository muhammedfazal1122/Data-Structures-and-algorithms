class Queue:
    array = []

    def Push(self):
        val=int(input("enter the value"))
        self.array.append(val)

        print(self.array)
    def Pop(self):
        self.array.pop(0)
        print(self.array)

obj = Queue()

while True:
    choice = int(input("Enter the number 1.ADD , 2.DEL, 3.Prin , 4. qqut"))
    # valuew = int(input("valuew;;;;;"))
    if choice==1:
        obj.Push()
    if choice==2:
        obj.Pop()