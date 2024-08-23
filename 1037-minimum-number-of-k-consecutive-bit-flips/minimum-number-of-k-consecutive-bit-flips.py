class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        current_flips = 0
        flip_markers = [0] * len(nums)  # To keep track of where flips start

        for i in range(len(nums)):
            if i >= k:
                current_flips ^= flip_markers[i - k]  # Adjust for flips that are no longer affecting the window

            # If current bit after considering previous flips is 0, we need to flip
            if (nums[i] ^ current_flips) == 0:
                if i + k > len(nums):
                    return -1  # If we can't flip k bits from current position
                flip += 1
                current_flips ^= 1  # Flip the current state
                flip_markers[i] = 1  # Mark this as the start of a flip

        return flip

















# #         flip = 0
# #         n = len(nums)
# #         for i in range(n):
# #             if nums[i]==0:
# #                 if i+k-1>=n:
# #                     return -1
# #                 for j in range(i,i+k):
# #                     if nums[j]==0:
# #                         nums[j]=1
# #                     else:
# #                         nums[j]=0
# #                     flip +=1
# #         return flip
# #         # q = deque()
# #         # n = len(nums)
# #         # for i in range(n):
# #         #     if q and q[0]<i:
# #         #         q.popleft()
# #         #     if len(q)%2==nums[i]:
# #         #         if i+k-1>=n:
# #         #             return -1
# #         #         q.append(i+k-1)
# #         #         flip+=1
# #         # return flip




# # from typing import List

# # class Solution:
# #     def minKBitFlips(self, nums: List[int], k: int) -> int:
# #         flip = 0
# #         n = len(nums)
# #         current_flips = 0
# #         flip_markers = [0] * n
        
# #         for i in range(n):
# #             if i >= k:
# #                 current_flips ^= flip_markers[i - k]
            
# #             if (nums[i] ^ current_flips) == 0:
# #                 if i + k > n:
# #                     return -1
# #                 flip += 1
# #                 current_flips ^= 1
# #                 if i < n:
# #                     flip_markers[i] = 1
        
# #         return flip













# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         flips = 0
#         for i in range(len(nums) - (k-1)):
#             if nums[i] == 0:
#                 flips += 1
#                 for i in range(i,i+k):
#                     if nums[i] == 0:
#                         nums[i] = 1
#                     else: 
#                         nums[i] = 0
#         return flips if nums.count(1) == len(nums) else -1
























#         # n = len(nums)
#         # flip = 0
#         # flips = [0] * n
#         # current_flips = 0
        
#         # for i in range(n):
#         #     if i >= k:
#         #         current_flips -= flips[i - k]
                
#         #     if (nums[i] + current_flips) % 2 == 0:
#         #         if i + k > n:
#         #             return -1
#         #         flip += 1
#         #         current_flips += 1
#         #         flips[i] += 1
        
#         # return flip
