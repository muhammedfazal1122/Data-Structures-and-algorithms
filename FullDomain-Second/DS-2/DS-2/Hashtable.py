class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=5):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size



    def insert_item(self, key, value, i=0): 
        index = self.hash_key(key)          

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            while self.arr[index] is not None:
                i += 1
                index = (self.hash_key(key) + i ** 2) % self.size
            self.arr[index] = Node(key, value)


    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.key, ":", current.value, " --> ", end="")
                    else:
                        print(current.key, ":", current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()




class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=5):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size

    def insert_item(self, key, value):
        index = self.hash_key(key)

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            while self.arr[index] is not None:
                index = (index + 1) % self.size
            self.arr[index] = Node(key, value)





    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.key, ":", current.value, " --> ", end="")
                    else:
                        print(current.key, ":", current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()




class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.ref = None


class HashTable:
    def _init_(self, size=2):
        self.arr = [None] * size
        self.size = size

    def hash_key(self, key):
        return hash(key) % self.size

    def insert_item(self, key, value):
        index = self.hash_key(key)

        if self.arr[index] is None:
            self.arr[index] = Node(key, value)
        else:
            current = self.arr[index]
            while current.ref:
                current = current.ref
            current.ref = Node(key, value)

    def delete_item(self, key):
        index = self.hash_key(key)
        current = self.arr[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    # Deleting the head node
                    self.arr[index] = current.ref
                else:
                    # Deleting a node that is not the head
                    prev.ref = current.ref
                return True  # Key found and deleted
            prev = current
            current = current.ref

        return False  # Key not found

    def print_table(self):

        for i in self.arr:
            if i is None:
                print("None")
            else:
                current = i
                while current:
                    if current.ref:
                        print(current.value, " --> ", end="")
                    else:
                        print(current.value)
                    current = current.ref


s = HashTable()
s.insert_item('sarath', 100)
s.insert_item('amal', 200)
s.insert_item('siva', 300)
s.insert_item('faza', 400)
s.insert_item('akash', 500)
s.print_table()