class Solution:
    def longestPalindrome(self, s: str) -> str:

        good_idx = 0
        good_len = 0

        for i in range(len(s)): # The idea is that each i serves as the new centre. Sometimes will be odd sometimes even

            # Case: when centering around i gives us an odd string
            l,r = i,i

            while l >= 0 and (r <= len(s) - 1) and s[l] == s[r]:

                if (r-l+1) > good_len:
                    good_len = r-l+1
                    good_idx = l
                
                l -= 1
                r += 1

            l,r = i,i+1

            while l >= 0 and (r <= len(s) - 1) and s[l] == s[r]:

                if (r-l+1) > good_len:
                    good_len = r-l+1
                    good_idx = l
                
                l -= 1
                r += 1

        return(s[good_idx:(good_idx + good_len)])
            


        