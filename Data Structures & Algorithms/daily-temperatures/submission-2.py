class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Start from right to left first and foremost

        # Our stack should keep track of the indices so when we want values
        # we just do value = temperatures[stack[-1]]

        # This makes it easier when we want distance later to do curr dist - stack

        # Monotonically DECREASING stack (only add stuff that is smaller)

        output_arr = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            
            # Just check that we have a stack and that curr temp BE first
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            # Then case when it's 
            if stack:
                output_arr[i] = stack[-1] - i 
            
            stack.append(i)
        
        return output_arr








        