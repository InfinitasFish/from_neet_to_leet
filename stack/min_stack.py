class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None or val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        item = self.stack[len(self.stack) - 1]

        self.stack.pop(len(self.stack) - 1)
        if item == self.min:
            if len(self.stack) == 0:
                self.min = None
            else:
                self.min = sorted(self.stack)[0]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min


inp = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(0)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())
