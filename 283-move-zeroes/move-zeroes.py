class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        first_index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[first_index]=nums[i]
                first_index+=1
        for i in range(first_index,len(nums)):
            nums[i]=0



