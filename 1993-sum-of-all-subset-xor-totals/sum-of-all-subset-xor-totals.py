class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, total):
            if i == len(nums):
                return total
            l = dfs(i+1, total ^ nums[i])
            r = dfs(i+1, total)
            return l + r
        
        return dfs(0,0)

















        # def dfs( i, total):
        #     if i == len(nums):
        #         return  total
        #     return dfs( i + 1, total ^ nums[i]) + dfs( i + 1, total)

        # return dfs( 0, 0)