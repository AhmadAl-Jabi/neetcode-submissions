class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Alright as we can see s1 will be smaller than or equal to s2 in length
        # We can maybe check for a window of size s1? And what I'm thinking is to store each char in s1 and their freqs
        # Then we work with the window in s2 always moving forward

        # I could've technically used hashmaps too here
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            s1_arr[index] += 1

        left = 0
        right = 0

        while right < len(s2):

            new_char_idx = ord(s2[right]) - ord('a')
            s2_arr[new_char_idx] += 1

            if s1_arr == s2_arr:
                return True
            
            right += 1

            if right - left == len(s1): # If we reached the point where window is of size s1 then we keep fixed size
                remove_idx = ord(s2[left]) - ord('a')
                s2_arr[remove_idx] -= 1
                left += 1
        
        
        return False
        
        