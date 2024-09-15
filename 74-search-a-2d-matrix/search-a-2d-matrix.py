
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows, cols = len(matrix), len(matrix[0])
#         top , bot = 0 , rows-1
#         while top <= bot:
#             row = (top + bot) // 2
#             if target > matrix[row][-1]:
#                 top = row + 1
#             elif target < matrix[row][0]:
#                 bot = row - 1
#             else:
#                 l, r = 0, cols - 1
#                 while l <= r:
#                     m = (l + r) // 2
#                     if target < matrix[row][m]:
#                         r = m - 1
#                     elif target > matrix[row][m]:
#                         l = m + 1
#                     else:
#                         return True  # Return True when target is found
#                 return False  # Return False if target is not found in the row
#         return False  # Return False if target is not found in the matrix




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        top , bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                l , r = 0, cols - 1
                while l <= r:
                    m = (l + r) // 2
                    if target < matrix[row][m]:
                        r = m - 1
                    elif target > matrix[row][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False