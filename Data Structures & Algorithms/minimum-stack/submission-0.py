class MinStack:

    # Each method must run in O(1) time !!!

    def __init__(self):
        # Initializes the stack object
        self.stack = []

        # We need a way to keep track of the smallest vals even when pop might remove the current smallest --> I'm thinking of a separate stack for that??

        # We can also maybe use a separate stack or something. O(1) lookup
        # Basically when popping we do it the same for both stacks
        # But when pushing we only push min(self.smallest[-1],val)
        # This way we pad the minimum multiple times since even if we pop multiple times we know that whatever we're popping is still not as small as the minimum we last added

        self.smallest = []

    def push(self, val: int) -> None:
        # pushes element val onto stack
        self.stack.append(val)

        if self.smallest: 
            self.smallest.append(min(val,self.smallest[-1])) 
        else:
            self.smallest.append(val)
        

    def pop(self) -> None:
        # removes top element from stack and doesn't return anything
        self.stack.pop()
        self.smallest.pop()
        

    def top(self) -> int:
        # GETS the top element of stack (doesn't remove it)
        return self.stack[-1]
        

    def getMin(self) -> int:
        # retrieves minimum element in stack (needs to be O(1))
        return self.smallest[-1]
        
