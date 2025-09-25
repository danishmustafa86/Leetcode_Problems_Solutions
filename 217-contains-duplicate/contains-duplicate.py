class Solution(object):
    def containsDuplicate(self, nums):

        numset = set(nums)
        return len(numset) != len(nums)

        # numset = set()

        # for n in nums:
        #     if n in numset:
        #         return True
        #     numset.add(n)
        # return False
        