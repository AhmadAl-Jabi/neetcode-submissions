class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # CAREFUL FOR DIV BY 0

        result = 0
        stack = []

        # Just go through tokens and each time we see a number append to the stack
        # When we see an operator (check for this first) we pop last two from stack, use operator on them (in right order) and then append result to stack

        # Rinse and repeat and be careful with any div by 0 (can return inf)
        # I think for division we just use floor div

        # We can have more than just 2 numbers bro so don't assume that

        # For subtraction and division we know that we gotta pop from left

        if len(tokens) == 1:
            return int(tokens[0])

        for char in tokens:

            if char in {"+", "-", "/", "*"}:

                right = stack.pop()
                left = stack.pop()

                if char == "+":
                    result = left + right
                    stack.append(result)

                elif char == "-":
                    result = left - right
                    stack.append(result)

                elif char == "*":
                    result = left * right
                    stack.append(result)

                elif char == "/":
                    result = int(left / right)
                    stack.append(result)
                
            else:
                stack.append(int(char))
        
        return result


        