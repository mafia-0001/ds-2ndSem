class DynamicArray:
    def __init__(self):
        self.data = []
        self.capacity = 1

    def append(self, x):
        if len(self.data) == self.capacity:
            self.capacity *= 2
        self.data.append(x)
        print("Size:", len(self.data), "Capacity:", self.capacity)

    def pop(self):
        if self.data:
            self.data.pop()

arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)