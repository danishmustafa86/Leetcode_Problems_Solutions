class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hsh = {val:val for val in nums}
        for i in range(len(nums) + 1):
            if i not in hsh:
                return i
