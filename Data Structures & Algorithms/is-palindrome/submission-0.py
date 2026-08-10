class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We just need a way to ignore/remove the whitespace between words (ignore is prob our best bet)

        # Start a left pointer at index 0 and right pointer at index len - 1
        left = 0
        right = len(s) - 1

        # While loop of as long as left <= right 
        # We ignore non alphanumeric chars
        # We do NOT care about case

        while left <= right:

            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Guaranteed to be alnum, just make sure we ignore case
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

        # If either left or right is white space we advance the specific one and skip the iteration