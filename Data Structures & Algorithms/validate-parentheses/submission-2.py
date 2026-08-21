class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for bracket in s:
            if bracket in valid_map:
                stack.append(valid_map[bracket])
            
            else:
                if len(stack) > 0 and stack[-1] == bracket:
                    stack.pop()
                
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False




        