class MyQueue:
    input_stack = list()
    output_stack = list()

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        #dump to output stack
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())
        #add to front
        self.input_stack.append(x)
        #dump it back to input stack
        while self.output_stack:
            self.input_stack.append(self.output_stack.pop())

    def pop(self) -> int:
        return self.input_stack.pop()
        

    def peek(self) -> int:
        val  = self.input_stack.pop()
        self.input_stack.append(val)
        return val
        

    def empty(self) -> bool:
        return not self.input_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()