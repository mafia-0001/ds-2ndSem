class Queue:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if len(self.q) == 0:
            return "Queue Underflow"
        return self.q.pop(0)

    def front(self):
        if len(self.q) == 0:
            return "Queue is empty"
        return self.q[0]


# Example
q = Queue()
q.push(10)
q.push(20)
q.push(30)

print("Front:", q.front())
print("Popped:", q.pop())
print("Queue:", q.q)