class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Only have to deal with uppercase letters
        # keep in mind the sliding approach where you decrease left until valid
        max_len = 0
        most_freq = 0 
        left, right = 0, 0
        # Keep a dictionary or bucket of unique characters?? and we can update it as we slide (dict[char] +=1 or -=1)
        freq_dict = {}

        # maybe we keep track of most_freq char (the string) and each time we move right we check if the window length - freq of most frequent is bigger than k. If so we cooked and we move left --> Make this check every time we hit the loop
        # "AABCBA" k = 2
        while right < len(s):

            # update char's count
            freq_dict[s[right]] = freq_dict.get(s[right],0) + 1

            # check that char at right has higher freq than most_freq. If so update
            if freq_dict.get(s[right]) > most_freq:
                most_freq = freq_dict[s[right]]

            # if window length - freq of most freq is bigger than k
            if (right - left + 1) - most_freq > k:
                # move left forward once and update (-1) the char
                freq_dict[s[left]] -= 1
                left += 1
                
        
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
        