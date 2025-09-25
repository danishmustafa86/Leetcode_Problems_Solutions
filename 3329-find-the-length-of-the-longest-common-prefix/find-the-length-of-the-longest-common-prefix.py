class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
            maxn = 0
            dic1 = {}
            for i in arr1:
                i = str(i)
                cur = ""
                for j in i:
                    cur += j
                    dic1[cur] = 1
            for i in arr2:
                i = str(i)
                cur = ""
                for j in i:
                    cur += j
                    if cur in dic1:
                        maxn  = max( maxn, len(cur))
            return maxn

            

















# class Solution:
#     def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#             maxn = 0
#             for i in arr1:
#                 for j in arr2:
#                     i = str(i)
#                     j = str(j)
#                     cur = 0
#                     for c1, c2 in zip( i , j):
#                         if c1 == c2:
#                             cur += 1
#                         else:
#                             break
#                     maxn = max( maxn, cur)
                    
#             return maxn