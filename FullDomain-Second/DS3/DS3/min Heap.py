class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i):
        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = (i - 1) // 2

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, i, n):
        smallest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest, n)

    def delete(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0, len(self.heap))
        return root

    def display(self):
        print("Min-Heap:", self.heap)

# Example usage
min_heap = MinHeap()

min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(15)
min_heap.insert(40)
min_heap.insert(50)
min_heap.insert(100)
min_heap.insert(25)
min_heap.insert(5)


min_heap.display()

min_deleted = min_heap.delete()

min_heap.display()
print("Deleted Min:", min_deleted)
