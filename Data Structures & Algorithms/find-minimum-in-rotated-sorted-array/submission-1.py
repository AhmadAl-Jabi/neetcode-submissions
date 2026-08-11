class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The items are all unique and were ORIGINALLY ordered 
        # We can basically do a binary search and look at left, mid and right each time
        # if mid smaller than left OR mid bigger than right then we know which half to pick --> right = mid or left = mid respectively until while left < right done

        # [5,6,1,2,3,4]

        left, right = 0, len(nums) - 1

        # worried about the case where two last items left (left and mid inf loop)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[left]:
                right = mid
                left += 1 # since we know left CANT be minimum
            
            elif nums[mid] > nums[right]:
                mid += 1
                left = mid

            else: # the arr is already in good order, take first item
                break

        return nums[left]
        