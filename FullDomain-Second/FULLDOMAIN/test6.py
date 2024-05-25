# list1=[1,2,3,4,5,6,7,8,9,10]
#
# list2=[x*2 if x%2==0 else x*3 for x in list1]
# print(list2)
#
# a=10
# b=20
# t=a if a>b else b


# duplicate=[]
# for i in range(len(list1)-1):
#     for j in range(i+1,len(list1)-1):
#         if list1[i]==list1[j]:
#             duplicate.append(list1[i])
#
# print(duplicate)


# list2=[x*2 for x in list1 if x%2==0]
# print(list2)
# list3=[x*3 for x in list1 if x%2==1]
# print(list3)



# dict1={'a':1,'b':2,'c':3}
# dict1['b']=5
#
# str1='fazal'

# dict2={}
# for c in str1:
#     if c in dict2:
#         dict2[c]+=1
#     else:
#         dict2[c]=1
# print(dict2)

# dict2={c:str1.count(c) for c in str1}
# print(dict2)

# myList=["python", "hub"]
#
# for i in myList:
#     myList.append(i.upper())
# print(myList)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def list1(self):
        s=[]
        current = self.head
        while current:
            s.append(current.data)
            current = current.next
        s.reverse()
        for i in range(len(s)):
            f=0
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    f=1
                    break
            if f==1:
                print('the last duplicate value is', s[i])
                break



# Creating a linked list with duplicate values
my_linked_list = LinkedList()
my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(8)
my_linked_list.append(2)
my_linked_list.list1()
# Displaying the linked list
my_linked_list.display()



