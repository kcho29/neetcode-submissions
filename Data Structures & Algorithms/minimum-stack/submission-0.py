class MinStack:

    def __init__(self):
        self.stack = []
        self.curmin = []

    def push(self, val: int) -> None:
        if not self.curmin:
            self.curmin.append(val)
        if val < self.curmin[-1]:
            self.curmin.append(val)
        else:
            self.curmin.append(self.curmin[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.curmin.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curmin[-1]