class Solution:
    def jump(self, nums: List[int]) -> int:
        lf,rt=0,0
        res=0
        while lf < (len(nums)-1):
            maxres=0
            for i in range(rt,lf+1):
                maxres=max(maxres,i+nums[i])
            rt=lf+1
            lf=maxres
            res+=1
        return res
