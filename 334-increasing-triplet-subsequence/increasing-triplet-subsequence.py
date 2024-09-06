class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = float("inf")
        second = float("inf")
        for val in nums:
            if val<= first:
                first = val
            elif val<= second:
                second = val
            else:
                return True
        return False






























        # if len(nums) < 3:
        #     return False
        
        # first = float("inf")
        # second = float("inf")
        # for val in nums:
        #     if val <= first:
        #         first = val
        #     elif val <= second:
        #         second = val
        #     else:
        #         return True
        # return False