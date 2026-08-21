class MinStack:

    def __init__(self):
        self.idx = 0
        self.arr = []
        self.min_num = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)

        if not self.min_num:
            self.min_num.append(val)
        elif val <= self.min_num[-1]:
            self.min_num.append(val)
        
        self.idx += 1
    
        
    def pop(self) -> None:
        new_num = self.arr.pop()

        if new_num == self.min_num[-1]:
            self.min_num.pop()

        self.idx -= 1

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_num[-1]
        
