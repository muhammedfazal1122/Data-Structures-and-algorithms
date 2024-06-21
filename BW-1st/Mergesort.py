#merge sort:

list1 = [1,3,8,5,43,2,3,5,6,89,4,2]

def mergesort(list1):
    if len(list1)>1:
        mid  = len(list1)//2
        leftlist = list1[:mid]
        rightlist = list1[mid:]
        mergesort(leftlist)
        mergesort(rightlist)

        i = k = j = 0
        while i< len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list1[k] = leftlist[i]
                i += 1
                k +=1
            else:
                list1[k] = rightlist[j]
                j += 1 
                k += 1 
        while i < len(leftlist):
            list1[k] = leftlist[i]
            i += 1 
            k += 1
        while j < len(rightlist):
            list1[k] = rightlist[j]
            j += 1
            k += 1

mergesort(list1)
print(list1)


