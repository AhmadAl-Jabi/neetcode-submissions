class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # This one is pretty easy. We basically just need to look at the sum of the two pointers (since sorted)
        # Then we basically just see if curr_sum is bigger than target (move right downward)
        # or if curr_sum is smaller than target (move left upward)
    
        # Until we hit the target :) and we return the two numbers in an array --> RETURN INDEX + 1

        left = 0
        right = len(numbers) - 1

        while left <= right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum < target:
                left += 1
                continue
            
            elif curr_sum > target:
                right -= 1
                continue

            return [left + 1, right + 1]

            
        