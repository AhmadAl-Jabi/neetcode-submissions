class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        #arith_map = {"+":ord(+), "-":ord(-), "*":ord(*), "/":ord(//)}
        stack = []
        final_result = 0

        for char in tokens:
            if char == "+":
                for num in stack:
                    final_result = final_result + num
                    stack.pop()
            
            elif char == "-":
                for num in stack:
                    final_result = final_result - num
                    stack.pop()
            
            elif char == "*":
                for num in stack:
                    final_result = final_result * num
                    stack.pop()
            
            elif char == "/":
                for num in stack:
                    final_result = final_result // num
                    stack.pop()

            else:
                stack.append(int(char))
                
        return final_result
        '''
    #   class Solution:
    #def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # "/"
                    # truncate toward zero
                    stack.append(int(a/b))
            else:
                stack.append(int(t))

        return stack[-1]
        