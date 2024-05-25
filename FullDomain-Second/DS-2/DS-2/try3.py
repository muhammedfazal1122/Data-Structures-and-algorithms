# def pivot_elemnt(list,first,last):
#     pivot=list[first]
#     left=first+1
#     right=last
#
#
#     while True:
#         while left<=right and list[left]<=pivot:
#             left=left+1
#         while left<=right and list[right]>=pivot:
#             right=right-1
#         if left>right:
#             break
#         else:
#             list[left],list[right]=list[right],list[left]
#     list[first],list[right]=list[right],list[first]
#     return right
#
# def quicksort(list,first,last):
#     if first<last:
#         p = pivot_elemnt(list, first, last)
#         quicksort(list, first, p - 1)
#         quicksort(list, p + 1, last)
#
#
# list=[9,8,7,44,65,5,4,433,34,4,5,5,6,6,7,8,89,9,32,6543]
# n=len(list)
# quicksort(list,0,n-1)
# print(list)


# def mergsort(list):
#      if len(list)>1:
#          mid=len(list)//2
#          left_list=list[:mid]
#          right_list=list[mid:]
#          mergsort(left_list)
#          mergsort(right_list)
#
#          i=0
#          k=0
#          j=0
#          while i<len(left_list) and j<len(right_list):
#              if left_list[i]< right_list[j]:
#                  list[k]=left_list[i]
#                  i=i+1
#                  k=k+1
#              else:
#                  list[k]=right_list[j]
#                  j=j+1
#                  k=k+1
#
#          while i<len(left_list):
#              list[k] = left_list[i]
#              i = i + 1
#              k = k + 1
#          while j<len(right_list):
#              list[k] = right_list[j]
#              j = j + 1
#              k = k + 1
#
# list=[9,8,7,44,65,5,4,433,34,4,5,5,6,6,7,8,89,9,32,6543]
# mergsort(list)
# print(list)
#

# def selection(list):
#     for i in range(len(list)-1):
#         min_intex=i
#         for j in range(i+1,len(list)):
#             if list[j]<list[min_intex]:
#                 min_intex=j
#         if list[i]!=list[min_intex]:
#             list[i],list[min_intex]=list[min_intex],list[i]
#
#
# list=[8,7,6,5,3,22,34,45,5,566,7,6,3993,5444,3,334,53]
# selection(list)
# print(list)

# list=[9,8,7,6,5,4,3,4,5,6,722,33,44,55,66,77,43]
# for i in range(len(list)):
#     pos=i
#     while list[pos]<list[pos-1] and pos>0:
#         list[pos-1],list[pos]=list[pos],list[pos-1]
#         pos=pos-1
#
# print(list)


list=[9,8,7,6,5,4,3,4,5,6,722,33,44,55,66,77,43]

def bubble(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

bubble(list)
print(list)







