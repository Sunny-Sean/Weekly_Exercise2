class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_k = []

    def is_empty(self):
        if len(self.stack_k) == 0:
            return True
        return False

    def is_full(self):
        if len(self.stack_k) == self.capacity:
            return True
        return False

    def push(self, value):
        if self.is_full():
            print("Can not add")
        else:
            self.stack_k.append(value)

    def pop(self):
        if self.is_empty():
            print("Can not pop")
        else:
            return self.stack_k.pop(-1)

    def top(self):
        return self.stack_k[-1]


stack1 = Stack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
