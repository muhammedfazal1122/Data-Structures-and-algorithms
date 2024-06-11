def bubble(arr):
    print(arr)
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list1=[8,7,6,5,4,3,55,66,77,3,322,112,22,33,4,454]

c=bubble(list1)
print(c)


