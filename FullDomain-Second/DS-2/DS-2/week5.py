def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]<list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list


list=[8,7,3,88,77,66,11,22,33,44]
bubbleSort(list)
print(list)