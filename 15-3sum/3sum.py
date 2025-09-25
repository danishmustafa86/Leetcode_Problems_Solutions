class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Set = set()
        Ans = []
        for i in range(len(nums) -2) :
            j = i + 1   // left pointer
            k = len(nums) - 1  // right pointer
            while j < k:   // from begining of j pointer to the end of nums which is k
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    Set.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        for i in Set:   // for converting set to array to fulfill function return type requirements
            Ans.append(i)
        return Ans


        





































        # ans = set()
        # res = []
        # nums.sort()
        # for i in range(len(nums) - 2):
        #     j = i+1
        #     k = len(nums) - 1
        #     while j < k:
        #         total = nums[i] + nums[j] + nums[k]
        #         if total == 0:
        #             ans.add((nums[i], nums[j], nums[k]))
        #             k -= 1
        #         elif total < 0:
        #             j += 1
        #         else:
        #             k -= 1
        # for i in ans:
        #     res.append(i)
        # return res















