#................Bubble sort...................

def bubblesort(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1)-1):
            if arr1[j]>arr1[j+1]:
                arr1[i],arr1[j]=arr1[j],arr1[i]

    return arr1

s=[23,5,65,7,8,89,6,5,45]
k=bubblesort(s)
print(k)


def selection(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    return arr

s=[23,5,65,7,8,89,6,5,45]
m=selection(s)
print(m)
#................insertion sort...................



def insertion(arr):
    for i in range(1,len(arr)):
        pos=i
        current=arr[i]
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current

    return arr

s=[23,5,65,7,8,89,6,5,45]
m=insertion(s)
print(m)



def bubblesort(arr, lenth):
    for i in range(length):

        for j in range(length - i):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [10, 50, 30, 11, 1, 6]
length = len(arr) - 1

print(bubblesort(arr, length))




def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [7, 4, 6, 98, 12, 55]

print(selectionsort(arr))



def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = i
        while key < arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = key
    return arr


arr = [8, 6, 0, 2, 1, 45, 12]
print(insertionsort(arr))
#
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        leftside = arr[: mid]
        rightside = arr[mid:]

        mergesort(leftside)
        mergesort(rightside)

        i = 0
        j = 0
        k = 0

        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside[j]:
                arr[k] = leftside[i]
                i += 1
                k += 1
            else:
                arr[k] = rightside[j]
                j += 1
                k += 1

        while i < len(leftside):
            arr[k] = leftside[i]
            k += 1
            i += 1

        while j < len(rightside):
            arr[k] = rightside[j]
            k += 1
            j += 1

    return arr


arr = [5, 7, 8, 3, 2, 4, 6, 1]
print(mergesort(arr))

def pivot_place(listt,first,last):
    pivot=listt[first]
    left=first+1
    right=last

    while True:
        while listt[left]<=pivot and left<=right :
            left=left+1
        while listt[right]>=pivot and left<=right :
            right=right-1
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












