def bubble(arr):
    print(arr)
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
list1=[3, 3, 4, 4, 5, 6, 7, 8, 22, 33, 55, 66, 77, 112, 322, 454]
c=bubble(list1)
print(c)


