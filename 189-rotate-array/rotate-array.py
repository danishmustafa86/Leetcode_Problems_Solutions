class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # k = k% len(nums)
        # nums[:] = nums[-k:] + nums[:-k]  # Modify nums in-place
        k = k% len(nums)
        while k > 0:
            deleted = nums[-1]
            del nums[-1]
            nums.insert(0, deleted)
            k -= 1

# Better if my upper answer not works
# 2nd one works I tested