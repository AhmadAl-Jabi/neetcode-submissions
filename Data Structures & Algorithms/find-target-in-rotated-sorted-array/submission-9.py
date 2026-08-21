'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Alright so we can define a left and right pointer (initialize to be beg and end)
        # Then we keep taking middle to be left + right // 2 as long as left < right
        # Then we just check that target is in between mid and right
        # If so then left = mid and right stays right
        # Else then left stays left and right becomes mid - 1

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


        