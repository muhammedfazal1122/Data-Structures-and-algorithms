

arr = [1,1, 3, 2, 7,2,3,3,3,3,3,4,4,4,4,4,45,5,10,5,66, 2, 10, 2, 3, 6, 9, 8, 10, 3, 7, 6,6]

i = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        if arr[i] == arr[j]:
            del arr[j]
        else:
            j +=1
    i += 1
    
print(arr)

