# def bublesort(arr):
#     l = len(arr)
#     for i in range(l-1):
#         for j in range(l-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
# print(bublesort(list1))

# def mergesort(arr):
#     if len(arr)>1:
#         mid = len(arr)//2
#         leftarr = arr[:mid]
#         rightarr = arr[mid:]

#         mergesort(leftarr)
#         mergesort(rightarr)

#         i = k = j = 0

#         while i < len (leftarr)  and j < len(rightarr) :
#             if leftarr[i]<rightarr[j]:
#                 arr[k] = leftarr[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = rightarr[j]
#                 j += 1
#                 k += 1
#         while i < len(leftarr) :
#             arr[k] = leftarr[i]
#             i += 1
#             k += 1
#         while j < len(rightarr):
#             arr[k] = rightarr[j]
#             j += 1
#             k += 1

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
# (mergesort(list1))
# print(list1)


# def pivote(list1, first, last):
#     pivot = list1[first]
#     left = first+1
#     right = last


#     while left < right and list1[left] <  pivot:
#         left += 1
#     while left  < right and list1[left] > pivot:
#         right += 1
#     list1[left],list1[right] = list1[right],list1[left]
#     if left > right:
#         list1[right],list1[first] = list1[first],list1[right]
#     return right

# def quicksort(list1, first, last):
#     if first<last:
#         p = pivote(list1,first,last)
#         quicksort( list1,first, p-1)
#         quicksort( list1,p+1, last)

# l = len(list1)
# (quicksort(list1, 0 ,l))
# print(list1)


# l = len(list1)
# i = 0
# while i < l:
#     pos = i
#     while pos > 0 and  list1[pos]< list1[pos -1]:
#         list1[pos],list1[pos -1] = list1[pos -1], list1[pos]
        # pos -= 1 
#     i += 1 

# print(list1)

# list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
  
# for i in range(len(list1)-1):
#     min_intex = i
#     for j in range(i+1,len(list1)):
#         if list1[j]< list1[min_intex]:
#             min_intex = j
#     if list1[i]!=min_intex:
#         list1[i],list1[min_intex]=list1[min_intex],list1[i]

# print(list1)


