class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = 0 
        stack = []
        for i, x in enumerate(nums + [-inf]): # append "-inf" to force flush all elements
            while stack and stack[-1][1] >= x: 
                _, xx = stack.pop()
                ii = stack[-1][0] if stack else -1 
                ans = max(ans, xx*(prefix[i] - prefix[ii+1]))
            stack.append((i, x))
        return ans % 1_000_000_007