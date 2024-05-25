# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.endOfWord = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
#             cur = cur.children[c]
#         cur.endOfWord = True
#
#     def search(self, word: str) -> bool:
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return cur.endOfWord
#
#     def startsWith(self, prefix: str) -> bool:
#         cur = self.root
#         for c in prefix:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return True
#
#
# # Create a Trie instance
# trie = Trie()
#
# # Insert words into the Trie
# trie.insert("apple")
# trie.insert("app")
# trie.insert("banana")
#
# # Search for words
# print(trie.search("apple"))  # True
# print(trie.search("app"))    # True
# print(trie.search("banana")) # True
# print(trie.search("grape"))  # False
#
# # Check if a prefix exists
# print(trie.startsWith("app"))    # True
# print(trie.startsWith("ban"))    # True
# print(trie.startsWith("orange")) # False

# class trienode:
#     def __init__(self):
#         self.childern={}
#         self.endofword=False
# class trie:
#     def __init__(self):
#         self.root=trienode()
#
#     def insert(self,word):
#         cur=self.root
#         for c in word:
#             if c not in cur.childern:
#                 cur.childern[c]=trienode()
#             cur=cur.childern[c]
#         cur.endofword=True
#
#     def search(self,word):
#         cur=self.root
#         for c in word:
#             if c not in cur.childern:
#                 return False
#             cur=cur.childern[c]
#         return cur.endofword
#
#     def startwith(self,prefix):
#         cur=self.root
#         for c in prefix:
#             if c not in cur.childern:
#                 return False
#             cur=cur.childern[c]
#         return True
#
# t=trie()
# t.insert('apple')
# t.insert('app')
# t.insert('animal')
# t.insert('ant')
# print(t.search('apple'))
# print(t.search('applee'))
# print(t.search('ante'))
# print(t.startwith('app'))