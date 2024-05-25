def linearsearch(arr,target):
    s=0
    for i in range(len(arr)):
        if arr[i]==target:
            s=1
            break
        else:
           s=0
    if s==1:
        print('found')
    else:
        print('not found')

a=[1,2,3,4,5,65,6,7,8,10]

linearsearch(a,50)


def binarysearch(arr,target,start,end):

    while start<end:

        mid=(start+end)//2

        if arr[mid]==target:
            return True

        elif target<arr[mid]:
            end=mid-1
        else:
            start=mid+1

        return binarysearch(arr,target,start,end)


a = [1,2,3,4,5,6,7,8,9,10]
end = len(a)-1
s = binarysearch(a,99,0,end)

if s == True:
    print('target found')
else:
    print('not found')


def binarysearch(arr,start,end,target):
    if  start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return True
        elif target<arr[mid]:
            end=mid-1
        else:
            start=mid+1

        return binarysearch(arr,start,end,target)


a=[1,2,3,4,5,6,7,8,9,10]
end=len(a)-1
s=binarysearch(a,0,end,10)
if s==True:
    print('found')
else:
    print('not found')

def binary_search(arr, target, start, end):
    if start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return True

        elif target < arr[mid]:
            return binary_search(arr, target, start, mid - 1)

        else:
            return binary_search(arr, target, mid + 1, end)

    return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(arr) - 1
result = binary_search(arr, 10, start, end)

if result:
    print('Target Found')

else:
    print('Target Not Found')


pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}
s = '{]([])}'
for i in s:
    print('this is in s :',i)
    if i in pairs:
        print('true')
        print(i)
    else:
        print('false')
        print(i)