class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isEndWord=True

class Bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            print("key is alredy present ")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=Bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=Bst(data)



