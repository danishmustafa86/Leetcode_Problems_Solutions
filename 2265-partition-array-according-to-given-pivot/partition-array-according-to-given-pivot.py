class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        num1, mid, num2 = [], [], []
        for i in range(len(nums)):
            if nums[i] < pivot:
                num1.append(nums[i])
            elif nums[i] == pivot:
                mid.append(nums[i])
            else:
                num2.append(nums[i])
        return num1 + mid + num2