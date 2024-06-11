
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
