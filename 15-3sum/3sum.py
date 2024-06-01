class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(len(nums)-2):
            j=i+1         #left pointer
            k=len(nums)-1 #right pointer
        
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    k-=1

                elif total>0:
                    k-=1

                else: # total<0
                    j+=1
        return ans
# time: O(n^2), space: O(1) in worst case O(n^2)