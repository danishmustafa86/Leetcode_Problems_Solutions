class Solution:
    def subsets(self, nums):
        ans = []
        def dfs( i, res):
            if i >= len(nums):
                ans.append(res[:])
                return
            dfs( i+1, res)
            res.append(nums[i])
            dfs( i+1, res)
            res.pop()
        dfs(0, [])
        return ans