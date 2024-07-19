class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0] :
            return 0
        if target > nums[-1]:
            return len(nums)
        # if target > nums[-1]:
        #     return len(nums)
        l,r = 0, len(nums)-1
        while l<=r:
            if target == nums[l]:
                return l 
            elif target == nums[r]:
                return r
            elif target < nums[l] and target > nums[l-1]:
                return l
            elif target < nums[r] and target > nums[r-1]:
                return r
            l += 1
            r -= 1
        return len(nums)