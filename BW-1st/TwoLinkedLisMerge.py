class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
    
class linkedist:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = newnode

    def print(self):
        if self.head is None:
            print('nooo') 
            return
        n = self.head
        while n is not None:
            print(n.data,"-->",end="")
            n = n.nref

    def oddDelete(self):
        n = self.head
        while n.nref is None:
            if n.data % 2 == 0 :
                n.nref = n.nref
            n = n.nref

    def merge_linked_list(left, right):
        if left.head is None:
            return right
        if right.head is None:
            return left
        
        node = left.head
        while node.nref:
            node= node.nref
        node.nref = right.head

        return left.head

    def mergeTwoLists(self, list1, list2):
        newlist = Node()
        current = newlist

        while list1 and list2:
            if list1.val < list2.val:
                current.nref = list1
                list1 = list1.nref
            else:
                current.nref = list2
                list2 = list2.nref
            current = current.nref

        if list1:
            current.nref = list1
        elif list2:
            current.nref = list2
        return newlist.nref


ll = linkedist()
ll.add(21)
ll.add(22)
ll.add(23)
ll.add(24)
ll.add(25)
ll.add(26)
ll.add(27)
ll.print()
