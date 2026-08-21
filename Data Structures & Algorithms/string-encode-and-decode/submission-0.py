class Solution:

    def encode(self, strs: List[str]) -> str:
        # I can maybe join all the strings together and make a set or array that has the indices where to split?

        self.arr = []
        old_idx = 0

        for item in strs:
            idx = len(item) + old_idx
            old_idx = idx
            self.arr.append(idx)

        return("".join(strs))

    def decode(self, s: str) -> List[str]:
        #Insert the whitespace at each index or maybe create new string just to perserve the idx
        #Then join them together into a list again

        new_arr = []
        old_idx = 0

        for idx in self.arr:
            new_arr.append(s[old_idx:idx])
            old_idx = idx

        return new_arr

