from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque([])
        self.minstack = deque([])

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack and self.minstack[-1]<=val:
            self.minstack.append(self.minstack[-1])
        elif self.minstack and self.minstack[-1]>val:
            self.minstack.append(val)
        self.stack.append(val)
        # print(self.stack,self.minstack)

    def pop(self) -> None:
        if self.minstack:
            a = self.minstack.pop()
        if self.stack:
            b = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
