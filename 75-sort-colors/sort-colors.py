class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lf,rt=0,len(nums)-1
        i=0
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        while i <= rt:
            if nums[i]==0:
                swap(i,lf)
                lf+=1
            elif nums[i] == 2:
                swap(i,rt)
                rt-=1
                i-=1
            i+=1
        return nums


        