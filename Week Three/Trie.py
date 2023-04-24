class Trie:
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

trie = Trie()
words = ['wait','waiter','shop','shopper']
for word in words:
    trie.add_word(word)

print(trie.does_word_exist('wait'))
print(trie.does_word_exist('sidh'))
print(trie.does_word_exist(''))
print(trie.does_word_exist('shop'))
print(trie.does_word_exist('shopper'))