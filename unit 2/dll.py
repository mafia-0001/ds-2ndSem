class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head:
            self.head.prev = new
            new.next = self.head
        self.head = new

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

dll = DLL()
dll.insert(10)
dll.insert(20)
dll.traverse()