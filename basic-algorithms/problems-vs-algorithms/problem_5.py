## Represents a single node in the Trie
class TrieNode:
    def __init__(self) -> None:
        ## Initialize this node in the Trie
        self.is_word   = False
        self.children  = {}
    
    def insert(self, char: str) -> None:
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def find_word(self, prefix):
        """Find all words starting with given prefix"""
        matches = []
        if self.is_word:
            matches += [prefix]
        for (char, node) in self.children.items():
            matches += node.find_word(prefix + char)

        return matches
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self) -> None:
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True


    def find(self, prefix: str) -> TrieNode | None:
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def match(self, prefix):
        # Return all matching words in the tree
        node = self.find(prefix)
        if node:
            return node.find_word(prefix)
        else:
            return []
    

# Test the hole implementation
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

assert MyTrie.match("p") == [] # Should return []
assert MyTrie.match("") == wordList

assert MyTrie.match("f") == ['fun', 'function', 'factory']  # Should return ['fun', 'function', 'factory']
assert MyTrie.match("fu") == ['fun', 'function'] # Should return ['fun', 'function']
assert MyTrie.match("func") == ['function']  # Should return ['function']
assert MyTrie.match("tri") == ['trie', 'trigger', 'trigonometry', 'tripod'] # Should return ['trie', 'trigger', 'trigonometry', 'tripod']
assert MyTrie.match("trig") == ['trigger', 'trigonometry'] # Should return ['trigger', 'trigonometry']

assert MyTrie.match("a") == ['ant', 'anthology', 'antagonist', 'antonym']
assert MyTrie.match("ant") == ['ant', 'anthology', 'antagonist', 'antonym']
assert MyTrie.match("anth")  ==  ['anthology']# Should return ['anthology']

