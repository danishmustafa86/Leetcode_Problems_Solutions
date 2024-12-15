class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        p1 = 0
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        return p1 + 1






        # p1, p2 = 0, 1
        # while p2 < len(nums):
        #     if nums[p2] == nums[p2 - 1]:
        #         p2 += 1
        #         continue
        #     p1 += 1
        #     nums[p1] = nums[p2]
        #     p2 += 1
        # return p1 + 1


        # p1 , p2 =0,1
        # while p2< len(nums):
        #     if nums[p2] == nums[p2-1]:
        #         p2 = p2 + 1
        #         continue
        #     p1 = p1+1
        #     nums[p1]=nums[p2]
        #     p2 = p2+1
        # return p1+1