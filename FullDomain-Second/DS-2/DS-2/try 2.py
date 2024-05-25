class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = 10
        self.table = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        newnode = Node(key, value)

        if self.table[index] is None:
            self.table[index] = newnode
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = newnode

    def display(self):
        for i in range(self.capacity):
            current = self.table[i]
            if current is not None:
                print(f'Bucket {i}:')
                while current:
                    print(f'{current.key}: {current.value}')
                    current = current.next
                print('------------------')

# Create an instance of HashTable
hashTable = HashTable()

# Insert elements
hashTable.insert(1, "John")
hashTable.insert(2, "Jane")
hashTable.insert(11, "Bob")
hashTable.insert(21, "Alice")

# Display the hash table
hashTable.display()
