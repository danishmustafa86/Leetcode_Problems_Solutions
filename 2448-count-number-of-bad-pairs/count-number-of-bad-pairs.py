from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        count = defaultdict(int)
        for i, num in enumerate(nums):
            ans += i - count[num - i]
            count[num - i] += 1
        return ans