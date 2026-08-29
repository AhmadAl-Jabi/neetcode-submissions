class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_string_map = {}
        # for each string we can do a bucket count of size 26 and then convert it to a tuple
        # maybe deal with case of empty string
        output_arr = []
        for string in strs:
            curr_arr = [0] * 26

            for char in string:
                index = ord(char) - ord("a")
                curr_arr[index] += 1
            
            curr_arr = tuple(curr_arr)

            if curr_arr in tuple_string_map:
                tuple_string_map[curr_arr].append(string)
            
            else:
                tuple_string_map[curr_arr] = [string]

        for key in tuple_string_map:
            output_arr.append(tuple_string_map[key])

        return output_arr        
        