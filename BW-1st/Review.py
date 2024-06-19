class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.isEndOfWord = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.isEndOfWord

    def autosearch(self,prefix):
        



