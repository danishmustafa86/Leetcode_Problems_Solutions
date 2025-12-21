class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l





















        
        # l, r = 0, len(nums)
        # while l < r:
        #     mid = (l+r) // 2
        #     if (target > nums[mid]):
        #         l = mid + 1
        #     else:
        #         r = mid
        # return l



















        # if  target < nums[0]:
        #     return 0
        # l, r = 0 , len(nums)-1
        # while l < r:
        #     mid = l+r//2
        #     if target < nums[mid]:
        #         r = mid -1 
        #     elif target > nums[mid]:
        #         l = mid 
        #     elif target == nums[mid]:
        #         return mid
        #     elif target > nums[mid] and target < nums[mid+1]:
        #         return mid 
        #     elif target > nums[mid] and target < nums[mid+1]:
        #         return mid 
        #     elif target > nums[mid] and target < nums[mid+1]:
        #         return mid 
        # return len(nums)
                

            
            