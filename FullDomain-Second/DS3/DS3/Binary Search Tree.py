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

    def search(self,data):
        if self.key==data:
            print("data found ")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("no data found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("no value found")
    def preOrderTraversal(self):

        print(self.key,end=" ")

        if self.lchild:
            self.lchild.preOrderTraversal()
        if self.rchild:
                self.rchild.preOrderTraversal()

    def inorderTraversal(self):
        if self.lchild:
            self.lchild.inorderTraversal()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorderTraversal()

    def postOrderTraversal(self):
        if self.lchild:
            self.lchild.postOrderTraversal()
        if self.rchild:
            self.rchild.postOrderTraversal()
        print(self.key,end=" ")

    def delete(self,data):
        if self.key is None:
            print("there os no value")
            return
        if self.key>data:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("there is no value to delete left")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("there is no value to delete in right")
        else:
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild

            node=self.rchild# take Right because its is a rule.
            while node.lchild:# and check search small element in this right node . only repace wiothe the small element in right child ,that's why we are taking the node.lchild(rightNode's leftchild)
                node=node.lchild   #that's why we are taking the node.lchild(rightNode's leftchild)
            self.key=node.key# changing the main node To that value of lchild or node)#nodes key goes to current's space            self.rchild=self.rchild.delete(node.key)#(NONE return= To change the deltionnode to NONE)

        return self#(return what we get from this recursiveFuncion or normal)


    def delete_only_if_two_child(self):
        if self.lchild is None and self.rchild is None:
            self.key = None
        elif self.lchild and self.rchild:
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)



    def clone(self):
        # Create a new tree with the same key
        
        new_tree = binaryserch(self.key)
        # Clone left subtree if it exists
        if self.lchild:
            new_tree.lchild = self.lchild.clone()
        
        # Clone right subtree if it exists
        if self.rchild:
            new_tree.rchild = self.rchild.clone()
        
        return new_tree





root=binaryserch(75)
list1=[6,5,63,58,15,79,35]
for i in list1:
    root.insert(i)
# root.search(10)
root.preOrderTraversal()
print(".")
root.inorderTraversal()
print(".")
root.postOrderTraversal()

print("clone:")
# root.delete_only_if_two_child()\
new = root.clone()
new.postOrderTraversal()


