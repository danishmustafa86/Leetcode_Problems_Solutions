class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        swapped = False
        n = len(nums)
        for i in range( n - 1):
            swapped = False
            for j in range( n - i - 1):
                if nums[j] > nums[j+1] and bin(nums[j]).count("1") == bin(nums[j+1]).count("1"):
                    swapped = True
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                elif nums[j] > nums[j+1] and bin(nums[j]).count("1") != bin(nums[j+1]).count("1"):
                    return False
            if swapped == False:
                break
        return True


