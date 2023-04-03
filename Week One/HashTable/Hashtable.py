class Hash:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
    def hashKey(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.hashKey(key)
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.hashKey(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.hashKey(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]


t = Hash()
t['january 12'] = 889
t['march 6'] = 234
t['march 17'] = 381

print(t['march 6'])

