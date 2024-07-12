class binaryserch:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key = data

        if self.key == data: 
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=binaryserch(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=binaryserch(data)

    def inorderTraversal(self):
        if self.lchild:
            self.lchild.inorderTraversal()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorderTraversal()

    def minn(self):
        curr = self
        while curr.lchild is not None:
            curr = curr.lchild
        return curr.key

    def maxx(self):
        curr = self
        while curr.rchild:
            curr = curr.rchild
        return curr.key

    def sum_min_max(self):
        return self.maxx()+ self.minn()

    closest = 0
    def find_closeset_element_of_target(self,data):
        if self.key==data:
            print("data found ")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.find_closeset_element_of_target(data)
            else:

                print("no data found")
                temp = self.key
                print(temp) 
        else:
            if self.rchild:
                self.rchild.find_closeset_element_of_target(data)
            else:
                temp = self.key



    def check_bst_inorder_helper(self):
        result = []
        
        if self.lchild:
            self.lchild.check_bst_inorder()
        result.append(self.key)
        if self.rchild:
            self.rchild.check_bst_inorder()
        return result

    def check_bst_inorder(self):
        
        result = self.check_bst_inorder_helper()

        for i in range(1,len(result)):
            if result[i-1] > result[i]:
                return False
        return True
         
            




root=binaryserch(75)
list1=[9,4,17,3,6,5,7,22,20]
for i in list1:
    root.insert(i)
# root.search(10)

root.inorderTraversal()
print('\n')
# print(root.minn())
print("...")
# print(root.maxx())
# print('\n')


print(root.check_bst_inorder())

# print(root.sum_min_max())
# print(root.find_closeset_element_of_target(18))