# listt=[8,2,6,9,1,4,9,2,4,8,23,1,8,7,65,4,3,35,6,7,8,3465,98,22,32,423,]
# for i in range(len(listt)-1):
#     min_index=listt.index(min(listt[i:]),i)
#     listt[i],listt[min_index] = listt[min_index],listt[i]

# print(listt)

listt=[8,7,6,5,3,22,34,45,5,566,7,6,3993,5444,3,334,53]
for i in range(len(listt)-1):  
    min_index = i
    for j in range(i+1, len(listt)):
        if listt[j] < listt[min_index]:
            min_index = j

    if listt[i] != listt[min_index]:
        listt[i], listt[min_index] = listt[min_index], listt[i]

print("Sorted Array:", listt)



