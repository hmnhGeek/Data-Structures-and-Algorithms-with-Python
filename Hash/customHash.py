class HashTable:
    def __init__(self, size):
        self.data = [[]]*size

    def _hash(self, key):
        # O(1)
        _h = 0
        for i in range(len(key)):
            _h = (_h + ord(key[i])*i) % len(self.data)

        return _h

    def set(self, key, value):
        # O(1)
        hs = self._hash(key)

        if self.data[hs] == []:
            self.data[hs] = [[key, value]]
        else:
            self.data[hs].append([key, value])

        return self.data

    def get(self, key):
        # O(1)
        hs = self._hash(key)
        bucket = self.data[hs]

        if bucket:
            for i in bucket:
                if i[0] == key:
                    return i[1]

        return None

    def keys(self):
        # O(n)
        _keys = []
        for i in self.data:
            if i != []:
                for j in i:
                    _keys.append(j[0])
        return _keys
