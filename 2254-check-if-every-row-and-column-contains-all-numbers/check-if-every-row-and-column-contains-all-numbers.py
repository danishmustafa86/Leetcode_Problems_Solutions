from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                if matrix[i][j] in row_set or matrix[j][i] in col_set:
                    return False
                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])
        if row_set != set(range(1,n+1)) or col_set != set(range(1,n+1)):
            return False
        return True