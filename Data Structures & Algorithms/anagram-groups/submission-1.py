class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #1: create a SET that stores dicts of each string, by idx, the dicts map the number of each char in the string

        #2: from that SET we take out subgroups of dicts that are equal to each other and store their matching strings 
        #in their own arrays (by index)

        #3: combine all the string subgroup arrays in a bigger array

        sorted_array = []
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
        
        for key in stored_dicts:
            sorted_array.append(stored_dicts[key])
        
        return sorted_array

        




        