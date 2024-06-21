class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heap_sort(self):
        n = len(self.arr)-1

        for intex in range(n // 2 - 1, -1, -1):
            self.heapify(n, intex)


        for intex in range(n - 1, 0, -1):
            self.arr[0], self.arr[intex] = self.arr[intex], self.arr[0]
            self.heapify(intex, 0) # index: when we swap elemnt with arr[0], now only want to sort unsorted arr, thats why index = n-1 in each iteration        



    def heapify(self, n, intex):
        print(n,intex)

        largest = intex
        print(largest)
        left = 2 * intex + 1
        right = 2 * intex + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != intex:
            self.arr[intex], self.arr[largest] = self.arr[largest], self.arr[intex]
            self.heapify(n, largest)



arr = [9,8,7,6,5,4,3,10]
print("Original array:", arr)

heap_sorter = HeapSort(arr)
heap_sorter.heap_sort()
print(arr)

