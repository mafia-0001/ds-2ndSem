class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return "Empty"
        return self.queue.pop(0)

    def front(self):
        return self.queue[0] if self.queue else "Empty"
#main
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
print(q.front())
