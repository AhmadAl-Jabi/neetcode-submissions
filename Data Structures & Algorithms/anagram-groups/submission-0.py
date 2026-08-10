class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Make a hashmap but have the keys as the 26 size array 
        #Anytime we encounter a string that fits a preexisting key, append to its array
        #in the end we just combine all the arrays into a bigger one

        anagrams_out = []
        group_anagrams = {}

        for i, x in enumerate(strs):
            # create size 26 empty key (we check later if already in dict)
            candidate_arr = [0]*26

            for char in x:
                candidate_arr[ord(char) - ord('a')] += 1

            key_candidate = tuple(candidate_arr) # needs to be a tuple to be a key
            if key_candidate in group_anagrams:
                group_anagrams[key_candidate].append(x)
            
            else:
                group_anagrams[key_candidate] = [x]

        anagrams_out = list(group_anagrams.values())

        return(anagrams_out)