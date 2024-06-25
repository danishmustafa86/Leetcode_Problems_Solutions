class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        array=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                array.append(i)
        return array[0],array[-1]