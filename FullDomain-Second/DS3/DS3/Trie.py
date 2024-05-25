class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("orange")) # Output: False

print(trie.startsWith("ban"))  # Output: True
print(trie.startsWith("bat"))  # Output: True
print(trie.startsWith("apl")) # Output: False
