class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # Initialize default to be 0s
        stack = [] # We need to pair [temp,idx]

        for i,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0] :
                idx_to_append = stack[-1][1]
                stack.pop() # Remove the smaller guy from stack
                result[idx_to_append] = i - idx_to_append
            
            stack.append([temp,i])
        
        return result



            
        