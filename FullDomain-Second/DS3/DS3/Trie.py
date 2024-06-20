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


    def auto_search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No matches found
            node = node.children[char]
        return self.search2(node, prefix)

    def search2(self, node, prefix):
        results = []  
        if node.isEndOfWord:
            results.append(prefix)
        for char, next_node in node.children.items():
            # Correctly extend the search from the next_node without passing it as an argument to self.search
            results.extend(self.search2(next_node, prefix + char))
        return results


    def delete(self, word):
        

        # Helper function for deletion
        def delete_recursively(node, word, depth):

            # Base case: If the node is None
            if not node:
                return False

            # If we have reached the end of the word
            if depth == len(word):
                # This node is no longer the end of the word
                if node.isEndOfWord:
                    node.isEndOfWord = False

                # If the node has no children, it can be deleted
                return len(node.children) == 0

            # Recursive case: Traverse the trie
            char = word[depth]
            if char in node.children:
                # If the child node can be deleted, delete it from the current node's children
                should_delete_child = delete_recursively(node.children[char], word, depth + 1)
                if should_delete_child:
                    del node.children[char]
                    # Return true if the current node has no children and is not the end of another word
                    return len(node.children) == 0 and not node.isEndOfWord

            return False

        # Start the deletion process from the root
        delete_recursively(self.root, word, 0)


# Example usage
trie = Trie()

words = ["fazal", "fazza", "hello world", "siva"]
for word in words:
    trie.insert(word)

# print(trie.auto_search("fazz"))

# print(trie.startsWith("faz")) 

# print(trie.search("app"))
# print(trie.search("fazal"))
# print(trie.search("fazza"))

print("---------AFTER---------------")
trie.delete("fazza")
print(trie.auto_search("faz"))
# print(trie.search("fazal"))  
# print(trie.search("fazza")) 