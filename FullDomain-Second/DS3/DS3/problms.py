class BST:
    # ... (rest of the class implementation)

    def mirror(self):
        self._mirror_recursive(self)

    def _mirror_recursive(self, node):
        if node:
            # Swap left and right subtrees
            node.left, node.right = node.right, node.left

            # Recursively mirror left and right subtrees
            self._mirror_recursive(node.left)
            self._mirror_recursive(node.right)

# ... (rest of the code remains unchanged)
# Example usage:
if _name_ == "_main_":
    root = BST(None)

    root.insertion(100)
    root.insertion(47)
    root.insertion(30)
    root.insertion(70)
    root.insertion(20)
    root.insertion(10)
    root.insertion(3)
    root.insertion(150)

    print("Before mirroring:")
    root.inorder()
    print()

    root.mirror()

    print("After mirroring:")
    root.inorder()
    print()


    def closeval(node, target):
        close_val = None
        min_diff = float("inf")
        while node:
            diff = abs(node.key - target)
            if diff < min_diff:
                min_diff = diff
                close_val = node.key
            if target < node.key:
                node = node.left
            else:
                node = node.right
        return close_val




    def even(self, num):
        return num % 2 != 0


    class TreeNode:
        def _init_(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    def inorder(root, array):
        if root is None:
            return

        inorder(root.left, array)
        array.append(root.val)
        inorder(root.right, array)


    def is_check(root):
        array = []
        inorder(root, array)

        for i in range(1, len(array)):
            if array[i] <= array[i - 1]:
                return False
        return True


    # Example usage
    # Construct the tree
    #        2
    #       / \
    #      1   3
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(1)

    print(is_check(tree))  # Output should be True for the provided tree


    class BinarySearchTree:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

        def insert(self, data):
            if self.key is None:
                self.key = data
                return

            if self.key == data:
                return
            if self.key > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BinarySearchTree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BinarySearchTree(data)

        def search(self, data):
            if self.key == data:
                print("Data found")
                return
            if self.key > data:
                if self.left:
                    self.left.search(data)
                else:
                    print("Data not found")
            else:
                if self.right:
                    self.right.search(data)
                else:
                    print("Data not found")

        def preOrderTraversal(self):
            print(self.key, end=" ")
            if self.left:
                self.left.preOrderTraversal()
            if self.right:
                self.right.preOrderTraversal()

        def inorderTraversal(self):
            if self.left:
                self.left.inorderTraversal()
            print(self.key, end=" ")
            if self.right:
                self.right.inorderTraversal()

        def postOrderTraversal(self):
            if self.left:
                self.left.postOrderTraversal()
            if self.right:
                self.right.postOrderTraversal()
            print(self.key, end=" ")

        def delete(self, data):
            if self.key is None:
                print("Tree is empty")
                return

            if data < self.key:
                if self.left:
                    self.left = self.left.delete(data)
                else:
                    print("Value not found")
            elif data > self.key:
                if self.right:
                    self.right = self.right.delete(data)
                else:
                    print("Value not found")
            else:
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                if self.right is None:
                    temp = self.left
                    self = None
                    return temp

                node = self.right
                while node.left:
                    node = node.left
                self.key = node.key
                self.right = self.right.delete(node.key)

            return self

        def inorder(self, array):
            if self is None:
                return

            if self.left:
                self.left.inorder(array)
            array.append(self.key)
            if self.right:
                self.right.inorder(array)

        def is_valid(self):
            array = []
            self.inorder(array)

            for i in range(1, len(array)):
                if array[i] <= array[i - 1]:
                    return False
            return True


    root = BinarySearchTree(75)
    list1 = [6, 5, 63, 58, 15, 79, 35]
    for i in list1:
        root.insert(i)

    print("pre order:")
    root.preOrderTraversal()
    print("\nInorder:")
    root.inorderTraversal()
    print("\npostorder:")
    root.postOrderTraversal()

    is_valid = root.is_valid()
    print("\nIs valid BST:", is_valid)




























