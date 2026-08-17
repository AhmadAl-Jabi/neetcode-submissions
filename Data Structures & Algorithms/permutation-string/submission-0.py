class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check until the counts are equal in s1 and the window of s2
        # otherwise return false. Also this forces the window size to be len(s1)

        left = 0
        freq_dict = {}
        s1_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        for right in range(len(s2)): # right is the moving index

            # update freq dict of new guy
            freq_dict[s2[right]] = freq_dict.get(s2[right],0) + 1

            # if window size is too small then just continue to next iteration
            if right - left + 1 < len(s1):
                continue

            # otherwise we just check that the dictionaries are the same
            if s1_dict == freq_dict:
                return True

            # if not then move left forward and update len
            freq_dict[s2[left]] -=1
            if freq_dict[s2[left]] == 0:
                freq_dict.pop(s2[left])
            left += 1 
        
        return False
            
            

        