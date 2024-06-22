class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # lf,rt=0,len(nums)
        # while lf<rt:
        #     if nums[lf]==0:
        #         del(nums[lf])
        #         nums.append(0)
        #         lf-=1
        #     lf+=1
        #     rt-=1

        # i=0
        # while i < len(nums):
        #     if nums[i]==0:
        #         del nums[i]
        #         nums.append(0)
        #     else: 
        #         i+=1


        # for i in range(len(nums)-1):
        #     if nums[i]==0:
        #         del(nums[i])
        #         nums.append(0)
        #         i-=1

        first_index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[first_index]=nums[i]
                first_index+=1
        for i in range(first_index,len(nums)):
            nums[i]=0





        """
        Do not return anything, modify nums in-place instead.
        """
        