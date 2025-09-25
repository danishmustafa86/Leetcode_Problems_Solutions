class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        def merge(left, right):
            sorted_array = []
            while left and right:
                if left[0] <= right[0]:
                    sorted_array.append(left.pop(0))
                else:
                    sorted_array.append(right.pop(0))
            sorted_array.extend(left)
            sorted_array.extend(right)
            return sorted_array
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        return merge_sort(nums)