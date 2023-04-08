class Hash:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def hash_key(self, key):
        h = 0
        for c in key:
            h += ord(c)
        return h % self.max
    
    def add(self,key, value):
        h = self.hash_key(key)
        self.arr[h] = value
    
    def get(self, key):
        h = self.hash_key(key)
        return self.arr[h]


has = Hash() 
has.add("march 6", 130)
print(has.get("march 6"))
