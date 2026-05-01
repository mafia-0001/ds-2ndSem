class DynamicArray:
    def __init__(self):
        self.data = []
    
    def append(self, x):
        self.data.append(x)
        print("Size:", len(self.data))

    def pop(self):
        if self.data:
            return self.data.pop()
        return "Empty"

arr = DynamicArray()
arr.append(10)
arr.append(20)
arr.pop()