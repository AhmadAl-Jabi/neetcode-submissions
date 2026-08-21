class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []

        for i in range(len(s)): # The idea is that each i serves as the new centre. Sometimes will be odd sometimes even

            # Case: when centering around i gives us an odd string
            l,r = i,i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                palindromes.append(s[l:r+1])
                
                l -= 1
                r += 1

            l,r = i,i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                palindromes.append(s[l:r+1])
                
                l -= 1
                r += 1

        return(len(palindromes))