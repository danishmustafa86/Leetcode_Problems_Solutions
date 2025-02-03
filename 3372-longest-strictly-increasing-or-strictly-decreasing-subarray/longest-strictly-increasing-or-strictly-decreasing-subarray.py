class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc , max_dec = 1,1
        cur_inc, cur_dec = 1,1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cur_dec += 1
                cur_inc = 1
            elif nums[i] > nums[i - 1]:
                cur_inc += 1
                cur_dec = 1
            else:
                cur_inc = cur_dec = 1

            max_inc = max( max_inc, cur_inc)
            max_dec = max( max_dec, cur_dec)
        
        return max( max_inc, max_dec)
