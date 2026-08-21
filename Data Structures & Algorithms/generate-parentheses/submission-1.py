class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        combinations = []
        num_open = 0
        num_closed = 0

        # NEED RECURSION FOR THIS

        # n is the number of pairs so the number of parentheses is 2n
        # We need to be careful with duplicates
        # Just looking at the problem it's quite evident that we'll need stacks here

        # Attempt
        # We limit ourselves to have equal amounts of open and close brackets (n of each)
        # A solution is valid as long as at ANY point, the diff between placed opens and closed
        # is 0 or positive. Basically can never have more closed placed than open 
        # (can also think of it as more closed in reserve than open)

        # How do we ensure that we hit all possibilities and don't get repetition?
        # I guess we can brute force and check that the string we come up with isn't in combinations yet
        # How do we even know how many is the max possibilities

        def backTracking(num_open,num_closed):

            if num_open == num_closed == n: # Base case where we exhausted everything
                result = "".join(stack)
                combinations.append(result)
                return
            
            if num_open < n: # We don't want an inf loop we can only add open till we run out
                stack.append("(")
                backTracking(num_open + 1, num_closed)
                stack.pop() # Intuitively we do this cuz once we go far and test we gotta come back and pop 
         
            if num_open > num_closed:
                stack.append(")")
                backTracking(num_open, num_closed + 1)
                stack.pop()
        
        backTracking(0,0)
        return combinations
        

        