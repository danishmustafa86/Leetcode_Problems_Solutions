class Solution:
    def subsets(self, nums):
        ans = []
        def dfs( i, res):
            if i >= len(nums):
                ans.append(res[:])
                return
            res.append(nums[i])
            dfs( i+1, res)
            res.pop()
            dfs( i+1, res)
        dfs(0, [])
        return ans