class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        stored_dicts = {}

        for i in range(len(strs)):
            # Map freq of letters using array of size 26
            my_arr = [0] * 26

            for char in strs[i]:
                # We use ascii of 'a' to be the reference 0 (max is z which is 25)
                index = ord(char) - ord('a')
                my_arr[index] += 1
            
            my_tuple = tuple(my_arr)

            if my_tuple not in stored_dicts:
                #In the dictionary we directly store the string as the value to the dict key
                stored_dicts[my_tuple] = []

            stored_dicts[my_tuple].append(strs[i])
        
        return list(stored_dicts.values())

        




        