class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def insertion(self, data):
        if self.key is None:
            self.key = data
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.key  and self.prime(self.key):
            print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

root = BST(10)

root.insertion(100)
root.insertion(50)
root.insertion(70)
root.insertion(47)
root.insertion(67)
root.insertion(19)
root.insertion(20)
root.insertion(167)
root.insertion(13)
root.insertion(30)
root.insertion(6)

root.inorder()