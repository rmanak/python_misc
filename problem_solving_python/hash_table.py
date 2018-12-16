class HashTable:
    """
    Very simple implementation of Hash Table using python lists
    """
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def hashfunction(self, key):
        return key % len(self.slots)

    def rehash(self, hashvalue):
        return (hashvalue + 1) % len(self.slots)

    def put(self, key, value):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        start = self.hashfunction(key)
        position = start
        data = None
        while self.slots[position] is not None:
            if self.slots[position] == key:
                data = self.data[position]
                break
            position = self.rehash(position)
            if position == start:
                break
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

myhash = HashTable()
myhash[1] = '1- hello'
myhash[2] = '2- this'
myhash[12] = '12- is'
print(myhash.data)
print(myhash[12])
myhash[321] = '321 - and'
print(myhash[320] is None)


