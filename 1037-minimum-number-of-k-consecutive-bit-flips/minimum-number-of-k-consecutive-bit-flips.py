# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         flip = 0
#         n = len(nums)
#         for i in range(n):
#             if nums[i]==0:
#                 if i+k-1>=n:
#                     return -1
#                 for j in range(i,i+k):
#                     if nums[j]==0:
#                         nums[j]=1
#                     else:
#                         nums[j]=0
#                     flip +=1
#         return flip
#         # q = deque()
#         # n = len(nums)
#         # for i in range(n):
#         #     if q and q[0]<i:
#         #         q.popleft()
#         #     if len(q)%2==nums[i]:
#         #         if i+k-1>=n:
#         #             return -1
#         #         q.append(i+k-1)
#         #         flip+=1
#         # return flip




from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        n = len(nums)
        current_flips = 0
        flip_markers = [0] * n
        
        for i in range(n):
            if i >= k:
                current_flips ^= flip_markers[i - k]
            
            if (nums[i] ^ current_flips) == 0:
                if i + k > n:
                    return -1
                flip += 1
                current_flips ^= 1
                if i < n:
                    flip_markers[i] = 1
        
        return flip
