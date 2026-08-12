class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Lowkey the EXACT same as the last problem except this time we check if target between not if min

        # [3,4,5,6,1,2]

        left, right = 0, len(nums) - 1

        # we check while left < right
        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid
                
                else:
                    left = mid + 1
        # then we calculate mid = (left + right) //2

        # we check if left <= mid 
            # true --> check that left <= target <= mid
                # true --> right = mid
                # else --> left = mid + 1
            
            else:
                if nums[right] >= target and target >= nums[mid]:
                    left = mid
                
                else:
                    right = mid - 1
            # false --> check that left >= target >= mid
                # true --> right = mid
                # else --> left = mid + 1
        
        if nums[left] == target:
            return left
        
        return -1
        