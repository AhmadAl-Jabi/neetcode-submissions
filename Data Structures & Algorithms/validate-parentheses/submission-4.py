class Solution:
    def isValid(self, s: str) -> bool:

        # We only have to worry about '(', '{' and '['

        # I can match the openers with their closers in a dictionary
        # Everytime I see an opener we append the closer to a stack
        # then if I see something NOT in the dict (O(n)) then we see if it's the last item of the stack and pop

        if len(s) <= 1:
            return False

        matching_dict = {'(': ')', '{': '}', '[': ']'}
        opener_stack = []

        for char in s:
            
            # If we see an opener
            if char in matching_dict:
                opener_stack.append(matching_dict[char]) # append the closer
                continue
            
            if len(opener_stack) == 0:
                return False
            
            # If we see a closer check that it's at the end of the stack
            if char == opener_stack[-1]:
                opener_stack.pop()
                continue
            
            else:
                return False
        
        if len(opener_stack) != 0:
            return False

        return True
 

        