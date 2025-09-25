class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        product_counts = defaultdict(int)
        for a,b in combinations(nums, 2):
            product_counts[a * b] += 1
        
        ans = 0
        for count in product_counts.values():
            if count >= 2:
                ans += comb(count,2) * 8

        return ans