from itertools import combinations
from math import comb
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        # Step 1: Precompute all products of pairs
        product_counts = defaultdict(int)
        for a, b in combinations(nums, 2):
            product_counts[a * b] += 1
        
        # Step 2: Count valid quadruples
        ans = 0
        for count in product_counts.values():
            if count >= 2:
                # Number of ways to choose 2 pairs from `count` pairs
                ans += comb(count, 2) * 8
        
        return ans