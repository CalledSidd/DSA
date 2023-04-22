class TrieOne:
    def __init__(self):
        self.root = {"*":"*"}
    def add_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = "*"

    def does_word_exist(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "*" in node


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False



class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, add):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        node.is_end_of_word = True

    def does_word_exist(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_end_of_word




trie = Trie()
words = ['wait','waiter','shop','shopper']
for word in words:
    trie.add_word(word)

print(trie.does_word_exist('wait'))
print(trie.does_word_exist('sidh'))
print(trie.does_word_exist(''))
print(trie.does_word_exist('shop'))
print(trie.does_word_exist('shopper'))