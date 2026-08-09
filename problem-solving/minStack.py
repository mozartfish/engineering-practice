class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            minVal = min(val, self.minStack[-1])
            self.minStack.append(minVal)
        else:
            self.minStack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
