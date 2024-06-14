class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new=[]
        for i in range(0,n):
            new.append(nums[i])
            new.append(nums[i+n])
        return new