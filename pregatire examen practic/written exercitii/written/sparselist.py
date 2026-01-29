class SparseList:
    def __init__(self):
        self.data: list[tuple] = []
        self.lastIndex = 0
        self.index = 0

    def set(self, index, value):
        found = False
        for i in range(len(self.data)):
            if self.data[i][0] == index:
                self.data[i] = (index, value)
                found = True
        if not found:
            self.data.append((index, value))
        self.lastIndex = max(index, self.lastIndex)
    def get(self, index):
        for item in self.data:
            if item[0] == index:
                return item[1]
        return None

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.lastIndex:
            raise StopIteration
        for item in self.data:
            if item[0] == self.index:
                self.index += 1
                return item[1]
        self.index += 1
        return 0

data = SparseList()
data.set(1, 1)
data.set(3, 2)
data.set(5, 3)
data.set(9, 99)
data.set(9, data.get(9) + 1)
for elem in data:
    print(elem, end=' ')