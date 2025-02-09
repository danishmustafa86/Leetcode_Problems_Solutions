# class Solution:
#     def countBadPairs(self, nums: List[int]) -> int:
#         ans = 0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if j - i != nums[j] - nums[i]:
#                     ans += 1
#         return ans


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        
        for i, num in enumerate(nums):
            # The number of good pairs is the number of times (nums[i] - i) has been seen before
            ans += i - count[num - i]
            # Update the count of (nums[i] - i)
            count[num - i] += 1
        
        return ans