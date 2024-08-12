class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if nums[i] == x:
                arr.append(i)
        res = []
        for i in range(len(queries)):
            if queries[i] <= len(arr):
                res.append(arr[queries[i]-1])
            else:
                res.append(-1)
        return res
            