class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_position = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[cur_position-2]:
                nums[cur_position] = nums[i]
                cur_position += 1


        return cur_position