class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # We're gonna use a sliding window AND set approach (set for O(1) lookup)
        max_length = 0
        unique_chars = set()

        # if s is empty just return 0 (edge case) --> always think edge cases
        if len(s) == 0:
            return 0

        left, right = 0, 0
        while right < len(s):
            
            while s[right] in unique_chars:
                unique_chars.discard(s[left])
                left += 1
            
            unique_chars.add(s[right])
            max_length = max(max_length, len(unique_chars))

            right += 1

        return max_length
        