class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        for i in range(len(nums)):
            isSorted = True
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    isSorted = False
            if isSorted:
                return True
            if not isSorted:
                val = nums.pop(0)
                nums.append(val)
        return False