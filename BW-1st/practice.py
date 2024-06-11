


# dict1 = {'a':[1,2,3,4], 'b':{'c':[1,2,3], 'd':[1]}}


    
         
# # output : [6, [[5, 4], 3], [2, 1]]
            
# list1 = [[1, 2], [3, [4, 5]], 6]

                

            


# print(list2)


# def outer_rev(list1):


    # def inner_reverse():

    # return 
                
# print(outer_rev(list1))    



class Node:
    def __init__(self,data) :
        self.data = data
        self.nref = None
    
class LinkedList:
    def __init__(self) :
        self.head = None
    

    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = newnode


    def prinnt(self):
        if self.head is None:
            print("empty")
        n = self.head
        while n is not None:
            print(n.data , "-->",end="",) 
            n = n.nref            





    def reverse(self):
      
        if self.head is None:
            print("there is no data")
            return
        prev = None
        current = self.head
        while current is not None:
            nextt = current.nref
            current.nref = prev
            prev = current
            current = nextt
        self.head = prev 







    def sum_of_3_mid(self):
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.nref
        mid = count//2
        i = 1      
        n = self.head
        while i <= mid-1:          
            n = n.nref
            i += 1
        prev = n.data
        midd = n.nref.data 
        next = n.nref.nref.data 

        return prev+midd+next

    def del_mid(self):
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.nref
        mid = count//2
        i = 1      
        n = self.head
        i = 1
        while i < mid:
            n = n.nref
            i += 1
        prev = n
        n.nref = n.nref.nref



lll = LinkedList()

lll.insert(11)
lll.insert(12)
lll.insert(13)
lll.insert(14)
lll.insert(15)
lll.insert(16)
lll.insert(17)
# c = lll.sum_of_3_mid()
# print(c)
lll.del_mid()
lll.prinnt()