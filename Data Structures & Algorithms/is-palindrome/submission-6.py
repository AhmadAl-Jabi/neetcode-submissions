class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Ok reversing the string and making a new string works fine but two pointer is more optimal here

        i = 0
        j = len(s) - 1
        s = s.lower()

        # Keep going until the two pointers collide
        while i < j:
            
            while not s[i].isalnum() and i<j:
                i += 1
            
            while not s[j].isalnum() and i<j:
                j -= 1
            
            if s[i] != s[j]:
                return False

            
            i += 1
            j -= 1
        
        return True