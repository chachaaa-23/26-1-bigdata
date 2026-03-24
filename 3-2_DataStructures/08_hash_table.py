class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None


h = HashTable()
h.put("apple", 100)
h.put("banana", 200)
h.put("papel", 300)
print(h.table)
print("apple:", h.get("apple"))
print("banana:", h.get("banana"))
print("papel:", h.get("papel"))
