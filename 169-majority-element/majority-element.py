class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh = {}
        for val in nums:
            if val not in hsh:
                hsh[val] = 1
            else:
                hsh[val] += 1
        count = 0
        maxCount=0
        for key, val in hsh.items():
            if val > maxCount:
                maxCount =val
                count = key
        return count

















        # nums.sort()
        # mid = nums[len(nums)//2]
        # return mid






        # nums.sort()
        # return nums[len(nums)//2]