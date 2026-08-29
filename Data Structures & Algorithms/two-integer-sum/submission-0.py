class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_pairings = {}
        # go through each number and see if target - curr in the hashmap --> if not just append curr 
        for i in range(len(nums)):
            curr_value = nums[i]
            complement = target - curr_value

            if complement in sum_pairings:
                return [sum_pairings[complement], i]
            
            sum_pairings[curr_value] = i

        # then when we do meet the match (e.g. 3 , 4 target 7) we would reach 4 and see 3 already in hashmap so we return the indices in order anyways 

        # the only issue I see is that you can have dupe entries but that literally doesn't matter since if it pairs with itself you'd just return first_instance, curr_instance and if they DON'T pair then you'd already have stored the first instance and ignore the second instance of it (e.g. [5,5,8] target = 13 --> [0,2]) BUT THIS WOULDN'T EVEN OCCUR BECAUSE WE'RE TOLD IT CAN'T HAPPEN
        