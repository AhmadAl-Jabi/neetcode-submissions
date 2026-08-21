class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Maybe we can store letters seen inside of a set

        letters_seen = set()

        left = 0
        right = 0

        # Default to 0
        longest_sub = 0

        while right < len(s):

            while s[right] in letters_seen:

                letters_seen.remove(s[left])
                left += 1


            letters_seen.add(s[right])
            
            new_length = len(letters_seen)

            if new_length > longest_sub:
                longest_sub = new_length
            
            right += 1
        
        return longest_sub
                

            
        