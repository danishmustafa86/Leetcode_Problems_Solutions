class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []
        for i in range(len(nums)):
            if nums[i] != val:
                arr.append(nums[i])
        for i in range(len(arr)):
            nums[i] = arr[i]

        return len(arr)

