
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


class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i):
        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = (i - 1) // 2

    def insert(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, i, n):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < n and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest, n)

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
        print("Max-Heap:", self.heap)


# Example usage
min_heap = MinHeap()
max_heap = MaxHeap()

min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(15)
min_heap.insert(40)
min_heap.insert(50)
min_heap.insert(100)
min_heap.insert(25)
min_heap.insert(5)

max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(40)
max_heap.insert(50)
max_heap.insert(100)
max_heap.insert(25)
max_heap.insert(200)

min_heap.display()
max_heap.display()

min_deleted = min_heap.delete()
max_deleted = max_heap.delete()

min_heap.display()
max_heap.display()
print("Deleted Min:", min_deleted)
print("Deleted Max:", max_deleted)
