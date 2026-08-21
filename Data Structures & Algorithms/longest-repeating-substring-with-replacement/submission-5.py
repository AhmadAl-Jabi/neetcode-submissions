class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Maybe we can use k as the width of the sliding window??

        # Some Notes:
         # We can create a dict that tracks how much of each char we have
         # Then basically we will consumne all of our replacements (k) with the most frequent char
         # This is where sliding window begins --> How?

        # Sliding attempt 1:
        # Start left and right at the beginning
        # Keep moving right forward until we get an instance of the thing
        # Make left and right 

        char_map = {}

        #for char in s:
        #    char_map[char] = 1 + char_map.get(char,0)

        left = 0
        right = 0
        max_count = 0
        most_freq = 0

        while right < len(s):

            char_map[s[right]] = 1 + char_map.get(s[right], 0)
            # len(substring) is just equal to right - left
            #eqn is : len(substring) - most_freq_char <= k --> basically if all chars are the same, then we have 0 <= k and no need to replace
            # if we reach a point where the above statement is NOT true then we simply shift left to the right by one and recalculate

            sub_length = right - left + 1
            most_freq = max(most_freq, char_map[s[right]]) # Rather than checking the max compared to everything in the dict, we only need to check the max between prev max and the new guy we changed
            
            new_longest = most_freq + k # + k is very important here

            if new_longest > max_count: # Basically if the most frequent showup plus the replacements we can make are more than last time
                max_count = new_longest 

            if sub_length - most_freq > k: # If we need to replace more characters than we are able to
                char_map[s[left]] = char_map.get(s[left]) - 1
                left += 1
                
            
            right += 1
        
        return min(max_count,len(s))
                 


        