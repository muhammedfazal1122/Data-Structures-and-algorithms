def bubbledown(arr, n, index):
    leftc = index * 2 + 1
    rightc = index * 2 + 2
    maxindex = index

    if leftc < n and arr[leftc] > arr[maxindex]:
        maxindex = leftc










    if rightc < n and arr[rightc] > arr[maxindex]:
        maxindex = rightc




    if maxindex != index:
        swap(arr, index, maxindex)
        bubbledown(arr, n, maxindex)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def build(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        bubbledown(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        bubbledown(arr, i, 0)

    return arr

# Example usage

unsorted_array = [91, 82, 72, 63, 54, 24, 33, 22, 112]
sorted_array = build(unsorted_array.copy())

print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
