class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue_k = []

    def is_empty(self):
        if len(self.queue_k) == 0:
            return True
        return False

    def is_full(self):
        if len(self.queue_k) == self.capacity:
            return True
        return False

    def enqueue(self, value):
        if self.is_full():
            print("Can not add")
        else:
            self.queue_k.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Can not pop")
        else:
            return self.queue_k.pop(0)

    def front(self):
        return self.queue_k[0]


queue1 = Queue(5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())