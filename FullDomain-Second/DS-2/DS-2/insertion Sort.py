def insertionSort(list):
    i=1
    while i<len(list):
        pos=i
        while list[pos]<list[pos-1] and pos>0:
            list[pos-1],list[pos]=list[pos],list[pos-1]
            pos -= 1
        i+=1


list=[8,7,6,5,4,3,55,66,77,3,322,112,22,33,4,454]
insertionSort(list)
print(list)

# ///////////////////////////////////////////////////////////////////////////////////

# def insertionSort(lst):
#     for i in range(1, len(lst)):
#         pos = i
#         while pos > 0 and lst[pos] < lst[pos - 1]:
#             lst[pos-1], lst[pos] = lst[pos], lst[pos-1]
#             pos -= 1

listt = [8, 7, 6, 5, 4, 3, 55, 66, 77, 3, 322, 112, 22, 33, 4, 454]

# insertionSort(listt)
# print(listt)

