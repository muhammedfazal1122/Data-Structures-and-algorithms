def pivot_place(listt,first,last):
    pivot=listt[first]
    left=first+1
    right=last

    while True:
        while listt[left]<=pivot and left<=right :
            left=left+1
        while listt[right]>=pivot and left<=right :
            right = right-1
        if right<left:
            break
        else:
            listt[left],listt[right]=listt[right],listt[left]

    listt[first],listt[right]=listt[right],listt[first]
    return right

def QuickSort(listt,first,last):
    if first<last:
        p=pivot_place(listt,first,last)
        QuickSort(listt,first,p-1)
        QuickSort(listt,p+1,last)


listt=[56,2,99,33,88,55,22,456,23,64,785,236,137]
n=len(listt)
QuickSort(listt,0,n-1)
print(listt)


# # //////////////////////////////////////////////////////////////////////////////////////////////////////////
# # list COMPRIHENTION:::::::::::::::::
# def quicksort(arr):
#     n = len(arr)
#     if n <= 1:
#         return arr

#     pivot = arr[n // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quicksort(left) + middle + quicksort(right)


# # Example usage:
# listt = [56, 2, 99, 33, 88, 55, 22, 456, 23, 64, 785, 236, 137]
# sorted_list = quicksort(listt)
# print(sorted_list)
