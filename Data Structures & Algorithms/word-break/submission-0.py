class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # keep in mind we can definitely use duplicates that's fine
        cache = [True] * len(s)

        # racecar
        #    3  6
        # race
        # r + ace
        # rac + e
        # race --> once we're at index x, are there ANY paths that lead us to the end

        # Plan
        # what does curr_idx mean --> The index we have explored thus far

        def dfs(curr_idx):
            # base cases: 

            # if our curr_idx == len(s) - 1 then return True (we would've only gotten here if the strings matched up until this point; no need to check that string1 == string2)
            if curr_idx == len(s) - 1:
                return True

            # if not cache[curr_idx] --> return cache[curr_idx] (no reason to explore this path)
            if not cache[curr_idx]:
                return cache[curr_idx]

            # loop over all options in wordDict
            for word in wordDict:
                # recursively explore options IF at current index we have len(s) - 1 >= curr_idx + len(option) AND s[curr_idx + 1: curr_idx + len(option) + 1] == option
                if len(word) + curr_idx <= len(s) - 1 and s[curr_idx + 1: curr_idx + len(word) + 1] == word:
                    # store result = dfs(option) --> check if true (short circuit True)
                    if dfs(curr_idx + len(word)):
                        return True

            # if none gave True then we set cache[curr_idx] = False and return False
            cache[curr_idx] = False
            return False
        
        return dfs(-1)


        