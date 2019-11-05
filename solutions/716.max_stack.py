class MaxStack:
    # Two stack
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        if not self.stack or x >= self.stack[-1][1]:
            self.stack.append((x,x))
        else:
            m = self.stack[-1][1]
            self.stack.append((x,m))
            
    def pop(self) -> int:
        return self.stack.pop()[0]
    
    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        temp = []
        m = self.peekMax()
        while self.top() != m:
            temp.append(self.pop())
        self.pop()
        
        while temp:
            self.push(temp.pop())
        return m
    
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()