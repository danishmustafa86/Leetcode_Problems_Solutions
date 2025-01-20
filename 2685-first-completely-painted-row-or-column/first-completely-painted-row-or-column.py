from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hsh = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hsh[mat[i][j]] = (i, j)

        n, m = len(mat), len(mat[0])
        row_count, col_count = [0] * n, [0] * m

        for idx in range(len(arr)):
            num = arr[idx]
            i, j = hsh[num]
            row_count[i] += 1
            col_count[j] += 1
            
            if row_count[i] == m or col_count[j] == n:  # Fixed condition
                return idx  # Fixed to return the index in `arr`

        return -1




















# class Solution:
#     def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
#         hsh = {}
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 hsh[mat[i][j]] = (i,j)

#         n, m = len(mat), len(mat[0])
#         row_count, col_count = [0] * n, [0] * m

#         for idx in range(len(arr)):
#             num = arr[idx]
#             i,j = hsh[num]
#             row_count[i] += 1
#             col_count[j] += 1
#             if row_count[i] == n or col_count[j] == m:
#                 return idx

#         return -1 

