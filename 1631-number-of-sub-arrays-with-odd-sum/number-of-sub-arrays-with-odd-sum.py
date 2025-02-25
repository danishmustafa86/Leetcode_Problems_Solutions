# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         coll = []
#         for i in range(len(arr)):
#             cur = 0
#             for j in range(i, len(arr) ):
#                 cur += arr[j]
#                 coll.append(cur)
#         ans = 0
#         for i in range(len(coll)):
#             if coll[i] % 2 == 1:
#                 ans += 1
#         return ans






from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Prefix sum starts with 0, which is even
        prefix_sum = 0
        ans = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                ans += odd_count  # Odd subarrays end here
                even_count += 1
            else:
                ans += even_count  # Even subarrays end here
                odd_count += 1
            
            ans %= MOD  # Ensure we don't exceed large values
        
        return ans



