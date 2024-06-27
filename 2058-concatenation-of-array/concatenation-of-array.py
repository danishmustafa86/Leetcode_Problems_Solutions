class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = []
        i,j = 0, 0
        while i < 2*(len(nums)):
            if i >= len(nums):
                array.append(nums[j])
                i += 1
                j += 1
            else: 
                array.append(nums[i])
                i += 1

        return array
