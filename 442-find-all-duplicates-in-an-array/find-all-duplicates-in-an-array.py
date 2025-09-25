class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        x = {}
        for val in nums:
            if val in x:
                arr.append(val)
            else:
                x[val] = 1
        return arr