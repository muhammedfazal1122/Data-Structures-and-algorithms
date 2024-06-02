


dict1 = {'a':[1,2,3,4], 'b':{'c':[1,2,3], 'd':[1]}}


    
         
# output : [6, [[5, 4], 3], [2, 1]]
            
list1 = [[1, 2], [3, [4, 5]], 6]

                

            


# print(list2)


def outer_rev(list1):


    def inner_reverse():

    return 
                
print(outer_rev(list1))    



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
        if self.head is not None:




    def reverse(self):
        n = self.head

        if n is None:
            print("there is no data")
            return
        prev = None
        while n.nef is not None:

            nextt = n.nref
            n.nref = prev
            prev = n
            n = nextt
