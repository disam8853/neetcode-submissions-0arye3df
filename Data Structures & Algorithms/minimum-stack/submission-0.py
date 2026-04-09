class MinStack:

    def __init__(self):
        self.minNum = []
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minNum:
            self.minNum.append(val if self.minNum[-1] > val else self.minNum[-1])
        else:
            self.minNum.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        self.minNum.pop()
        return val

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minNum[-1]
