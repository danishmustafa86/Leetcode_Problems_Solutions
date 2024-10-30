class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        for i in ans:
            res.append(i)
        return res
