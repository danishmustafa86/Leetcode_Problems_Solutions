class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]
        return mid





        # hsh = {}
        # for val in nums:
        #     if val not in hsh:
        #         hsh[val] = 1
        #     else:
        #         hsh[val] += 1
        


















        # nums.sort()
        # return nums[len(nums)//2]