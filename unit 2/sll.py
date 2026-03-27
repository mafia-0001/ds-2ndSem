class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data")
            temp = temp.next
#main
ll = SLL()
ll.insert(10)
ll.insert(20)
ll.traverse()
