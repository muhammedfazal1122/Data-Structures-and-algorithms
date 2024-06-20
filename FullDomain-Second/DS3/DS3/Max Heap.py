class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, value): 
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.heap[index] <= self.heap[parentIndex]:
                break
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            index = parentIndex

    def extract_max(self):
        if not self.heap:
            raise Exception("Heap is empty!")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_val


    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)



maxHeap = MaxHeap()

maxHeap.insert(15)
maxHeap.insert(20)
maxHeap.insert(7)
maxHeap.insert(9)
# maxHeap.insert(44)
# maxHeap.insert(30)
maxHeap.extract_max()
print("Max Heap after extraction:", maxHeap.heap)
