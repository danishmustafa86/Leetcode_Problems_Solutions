from collections import Counter
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Count occurrences of each number in nums
        hsh = Counter(nums)

        # Range compression with prefix sums
        range_count = Counter()
        for num, count in hsh.items():
            # Increment range [num - k, num + k]
            range_count[num - k] += count
            range_count[num + k + 1] -= count

        # Find the maximum beauty using a sliding range sum
        max_beauty = 0
        current_beauty = 0
        for key in sorted(range_count):
            current_beauty += range_count[key]
            max_beauty = max(max_beauty, current_beauty)

        return max_beauty
