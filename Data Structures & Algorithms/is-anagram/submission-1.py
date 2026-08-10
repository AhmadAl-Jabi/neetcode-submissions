class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The count of characters is what we care about --> not order
        # Can do with arrays (since 26 letters) or compare 2 dicts

        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i],0)
            t_dict[t[i]] = 1 + t_dict.get(t[i],0)

        return True if s_dict == t_dict else False
       