class MyStack:
    def __init__(self):
        self.stack_in = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        return self.stack_in.pop()

    def top(self) -> int:
        return self.stack_in[-1]
    
    def empty(self) -> bool:
        return not self.stack_in
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()