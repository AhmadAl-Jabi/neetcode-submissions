class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # Initialize default to be 0s
        stack = [] # We need to pair [temp,idx]

        # The main thing here that was tripping me up initially is just the fact that I gotta track the index of everything
        # It seemed so confusing to me and it seemed like something only a dict could solve but I forget that there's 
        # Such a simple alternative where you can just append [temp,idx] pairs and enumerate through the temperatures to get idx and temp

        # Another thing is to zero intiialize the entire result array so that we can easily do arr[idx] = smt since sometimes we might 
        # Have the answer to arr[3] before we have the answer to arr[1] if arr[3] is smaller for example

        for i,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0] :
                idx_to_append = stack[-1][1]
                stack.pop() # Remove the smaller guy from stack
                result[idx_to_append] = i - idx_to_append
            
            stack.append([temp,i])
        
        return result



            
        