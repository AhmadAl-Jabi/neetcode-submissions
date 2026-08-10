class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Since the arr is sorted we can simply have two pointers and check the middle of the two (floor average --> left + right // 2)
        # If middle bigger than target then we make right = middle - 1
        # if smaller we make left = middle
        # else we return the index of the guy if theres a match

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                right = middle - 1
            
            else:
                left = middle + 1

        # If we don't find return -1
        return -1
        