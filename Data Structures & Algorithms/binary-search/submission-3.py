class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Set pointers on left and right sides of array
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid_pt = int((left + right) / 2)

            if nums[mid_pt] == target:
                return mid_pt

            elif target > nums[mid_pt]:
                left = mid_pt + 1

            else:
                right = mid_pt - 1

        return -1